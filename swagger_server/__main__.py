#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import os


def main(env=None):
    print(os.environ)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    yaml_file_name = ''
    if env is None:
        yaml_file_name = 'swagger_prod.yaml'
    else:
        yaml_file_name = 'swagger_dev.yaml'
    app.add_api(yaml_file_name, arguments={'title': 'Swagger Petstore'})
    return app

application = main()

if __name__ == '__main__':
    main('DEV').run(port=8080)
