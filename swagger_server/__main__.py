#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import os


def main():
    env = ''
    if "APP_ENV" in os.environ:
        env = os.environ['APP_ENV']

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    yaml_file_name = 'swagger_local.yaml'
    if env == 'PROD':
        yaml_file_name = 'swagger_prod.yaml'
    elif env == 'DEV':
        yaml_file_name = 'swagger_dev.yaml'
    elif env == 'TEST':
        yaml_file_name = 'swagger_test.yaml'

    app.add_api(yaml_file_name, arguments={'title': 'Swagger Petstore'})
    return app

application = main()

if __name__ == '__main__':
    main().run(port=8080)
