from flask import Blueprint, jsonify, request
from services.config import db
from services.models import *


api = Blueprint('api', __name__)

