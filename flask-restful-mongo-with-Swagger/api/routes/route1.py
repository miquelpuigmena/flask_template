import json
from http import HTTPStatus
from flask import Blueprint, request, abort
from flask_restful import Resource
from logger.logger import LoggerHelper
from models.model1 import ModelReferenced1


class Route1(Resource):

    LOGGER = LoggerHelper.get_logger(name=__name__, filename=__name__ + ".log")

    def get(self, id='No param provided'):
        """
        GET method

        :return:
        """
        try:
            return "GET Inside route1 - " + str(id), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(ex))

    def post(self):
        """
        POST method

        :return:
        :raises:
        """
        try:
            body = request.get_json(force=True)
            ModelReferenced1(ref_param1="uno", ref_param2="dos").save()
            body["response"] = "ModelReferenced1 successfully stored"
            return json.dumps(body), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))
