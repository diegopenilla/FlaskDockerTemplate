# launches app and other app tasks
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# common to all configs 
class Config(object):
    # to be defined in environment 
    SECRET_KEY = '\x98s+\xec\x90\x176U\xfa\xb4\xca\xd8K\x08\xfd\xa9\xa6?\xf2\x00\x0b\xe5\xd5\xf7'
    # Prometheus Directory
    #PROMETHEUS_MULTIPROC_DIR = os.getenv('prometheus_multiproc_dir')

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    DEBUG=True
    TESTING=True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}