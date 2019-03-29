import json
from http import HTTPStatus
from flask import Blueprint, request, abort
from logger.logger import LoggerHelper
from db.database import db_session
from db.models.model2 import Model2

BLUEPRINT_NAME = "bp2"
bp2 = Blueprint(BLUEPRINT_NAME, __name__)
LOGGER = LoggerHelper.get_logger(name=BLUEPRINT_NAME, filename=BLUEPRINT_NAME+".log")


@bp2.route("/")
def get_home():
    """
    GET method

    :return: String
    """
    m1 = Model2(name="bp2", email="bp2@")
    db_session.add(m1)
    db_session.commit()
    return "GET Inside blueprint2"


# @require_role(Roles.VNO)
@bp2.route("/", methods=['POST'])
def post_home():
    """
    POST method

    :return: Json
    :raises:
        - HTTP
    """
    try:
        body = request.get_json(force=True)
        body["response"] = "POST Inside blueprint2"
        return json.dumps(body), HTTPStatus.ACCEPTED
    except Exception as ex:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(ex))
