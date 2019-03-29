import json
from flask import Blueprint, request, abort
from logger.logger import LoggerHelper
from db.database import db_session
from db.models.model1 import Model1

# from helpers.authorization import require_role, Roles

BLUEPRINT_NAME = "bp1"
bp1 = Blueprint(BLUEPRINT_NAME, __name__)
LOGGER = LoggerHelper.get_logger(name=BLUEPRINT_NAME, filename=BLUEPRINT_NAME+".log")


@bp1.route("/")
def get_home():
    """
    GET method

    :return:
    """
    m1 = Model1(name="bp1", email="bp1@")
    db_session.add(m1)
    db_session.commit()
    return "GET Inside blueprint1"


# @require_role(Roles.VNO)
@bp1.route("/", methods=['POST'])
def post_home():
    """
    POST method

    :return:
    :raises:
    """
    try:
        body = request.get_json(force=True)
        body["response"] = "POST Inside blueprint1"
        return json.dumps(body), 202
    except Exception as ex:
        abort(500, str(ex))
