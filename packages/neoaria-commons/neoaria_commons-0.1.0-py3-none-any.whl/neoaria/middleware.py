import logging, requests, yaml, time, jwt
from logging.handlers import SysLogHandler
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from jwt import PyJWTError


class PerformanceMonitoringMiddleware(BaseHTTPMiddleware):

    logger = logging.getLogger("performance_logger")
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        
        self.logger.info(f"Request processed in {process_time:.4f} seconds")

        return response
    
class JWTMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, config: dict):
        super().__init__(app)
        if config['enabled'] == True:
            self.secret_key = config['secret_key']
            self.algorithm = config['algorithms']

    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
                request.state.user = payload
            except PyJWTError:
                raise HTTPException(status_code=401, detail="Invalid token")
        else:
            raise HTTPException(status_code=401, detail="Authorization header missing")
        
        response = await call_next(request)
        return response

class HTTPLogHandler(logging.Handler):
    def __init__(self, log_server_url):
        super().__init__()
        self.log_server_url = log_server_url

    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post(self.log_server_url, json={"log": log_entry})
        except Exception as e:
            print(f"Failed to send log to server: {e}")

class RequestLoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, log_level: int = logging.INFO, include_headers: bool = False, config: dict = None):
        
        super().__init__(app)

        if config['type'] == 'http':
            self.log_handler = HTTPLogHandler(f'http://{config['servers']['http']['host']}:{config['servers']['http']['port']}/{config['servers']['http']['endpoint']}')
        else:
            self.log_handler = SysLogHandler(address=(config['servers']['syslog']['host'],  config['port']))

        self.log_handler.setFormatter(logging.Formatter(config['format']))

        self.logger = logging.getLogger("request_logger")
        self.logger.addHandler(self.log_handler)
        self.logger.setLevel(log_level)

    async def dispatch(self, request: Request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        
        self.logger.log(self.logger.level, f'{request.method} {request.url} {response.status_code}')

        print(f"Response: {response.status_code}")
        return response

def setupMiddleware(fastApi: FastAPI):

    config_yaml = load_middleware_config() 
    __setup_middleware(config_yaml, fastApi)

def load_middleware_config() -> dict:
    with open('config/middleware.yaml', 'r') as file:
        return yaml.safe_load(file)

def __setup_middleware(config_yaml: dict, fastApi: FastAPI):
    
    if 'logging' in config_yaml:
        __setup_logging__(config_yaml, fastApi)

    if 'jwt' in config_yaml:
        __setup_jwt__(config_yaml, fastApi)

    if 'gzip-response' in config_yaml:
        __setup_gzip__(config_yaml, fastApi)
    
    if 'cors' in config_yaml:
        __setup_cors__(config_yaml, fastApi)
    
    if 'performance-monitor' in config_yaml:
        __setup_performance_monitor__(config_yaml, fastApi)

def __setup_logging__(config_yaml: dict, fastApi: FastAPI):
    logging_yaml = config_yaml['logging']

    if logging_yaml['enabled']:
        
        check_level = logging_yaml['level'].upper()

        if check_level == 'INFO':
            log_level_type = logging.INFO
        elif check_level == 'WARNING':
            log_level_type = logging.WARNING
        elif check_level == 'ERROR':
            log_level_type = logging.ERROR
        elif check_level == 'CRITICAL':
            log_level_type = logging.CRITICAL
        else:
            log_level_type = logging.DEBUG

        fastApi.add_middleware(RequestLoggingMiddleware, 
            log_level=log_level_type, 
            include_headers=logging_yaml['include_headers'], 
            config=logging_yaml)

def __setup_jwt__(config_yaml: dict, fastApi: FastAPI):
    logging_yaml = config_yaml['jwt']
    if logging_yaml['enabled']:
        fastApi.add_middleware(JWTMiddleware, 
                                    config=logging_yaml)

def __setup_gzip__(config_yaml: dict, fastApi: FastAPI):
    logging_yaml = config_yaml['gzip-response']
    if logging_yaml['enabled']:
        fastApi.add_middleware(GZipMiddleware, 
            minimum_size=logging_yaml['minimum_size'])

def __setup_cors__(config_yaml: dict, fastApi: FastAPI):

    logging_yaml = config_yaml['cors']
    if logging_yaml['enabled']:
        fastApi.add_middleware( CORSMiddleware,
            allow_origins=logging_yaml['allow_origins'],
            allow_credentials=logging_yaml['allow_credentials'],
            allow_methods=logging_yaml['allow_methods'],
            allow_headers=logging_yaml['allow_headers'])

def __setup_performance_monitor__(config_yaml: dict, fastApi: FastAPI):
    pass
