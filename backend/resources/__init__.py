from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, Response
import click
from common import configs
from common.exts import db, cors, api, docs
from models.book import BooksModel
from blueprints.book_routes import book as book_bp
from resources import book_resources

app = Flask(__name__)
app.config.from_object(configs)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask Restful API project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SPEC_URL': '/swagger',
    'APISPEC_SPEC_UI_URL': '/swagger-ui'

})
db.init_app(app)
cors.init_app(app)
api.init_app(app)
docs.init_app(app)


# app.register_blueprint(book_bp)


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    BooksModel().init_db()
    click.echo(' Generating data.....')


@app.route('/swagger.yaml', methods=["GET"])
def gen_swagger_yaml():
    yaml_spec = docs.spec.to_yaml()
    return Response(yaml_spec, mimetype="text/yaml")