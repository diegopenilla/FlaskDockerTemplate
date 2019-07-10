"""
Factory Function to initialize the Application
    - Configures the app using the env variable FLASK_CONFIG:
        - specifies settings to be taken from config.py
        - defined by cmd.sh file
    - Registers an api blueprint and a normal flask blueprint
    - Called by flask run or gunicorn in cmd.sh
"""
import os
from flask import Flask
from config import config
from flask_restplus import apidoc

# import configuration from config.py

def create_app(config_name=os.getenv('FLASK_CONFIG')):
    """ Initializes app
    
    Keyword Arguments:
        config_name {[str]} -- 'development', 'testing' or 'production'
    
    Returns:
        [Flask] -- the web application object
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    print(app.config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import flask blueprints from blueprints folder:
    from .blueprints import main
    app.register_blueprint(main.bp)

    # import api blueprints from apis folder:
    # Swagger UI in <server_url>/api/doc 
    from .apis import main_api
    app.register_blueprint(main_api.main_blueprint)

    # example of adding another blueprint
    # Swagger UI in <server_url>/api2/doc
    from .apis import second_api
    app.register_blueprint((second_api.second_blueprint))
    return app
