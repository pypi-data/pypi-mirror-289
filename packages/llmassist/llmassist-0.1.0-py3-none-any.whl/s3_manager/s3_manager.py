import logging
import os
from functools import wraps
from .parameter_config import LogConfig

class S3Manager:  
    def init(s3_path):
        print(s3_path)

