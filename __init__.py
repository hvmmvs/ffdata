from flask import Flask, url_for, render_template, jsonify, request, redirect,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth
from werkzeug import secure_filename
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__, template_folder ="frontend/templates",
                static_folder="frontend/static")

# auth = HTTPBasicAuth()
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)