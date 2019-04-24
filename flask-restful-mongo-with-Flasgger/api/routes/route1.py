import json
from http import HTTPStatus
from flasgger.utils import swag_from
from flask import Blueprint, request, abort
from flask_restful import Resource
from logger.logger import LoggerHelper
from models.model1 import BasicModel1


class Route1(Resource):

    LOGGER = LoggerHelper.get_logger(name=__name__, filename=__name__ + ".log")

    @swag_from("/swagger/route1/get.yaml")
    def get(self, id='No param provided'):
        try:
            return "GET Inside route1 - " + str(id), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))

    @swag_from("/swagger/route1/post.yaml")
    def post(self):
        try:
            body = request.get_json(force=True)
            BasicModel1(ref_param1="uno", ref_param2="dos").save()
            body["response"] = "ModelReferenced1 successfully stored"
            return json.dumps(body), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))

