import json
from http import HTTPStatus
from flasgger.utils import swag_from
from flask import Blueprint, request, abort
from flask_restful import Resource
from logger.logger import LoggerHelper


class Route2(Resource):

    LOGGER = LoggerHelper.get_logger(name=__name__, filename=__name__ + ".log")

    @swag_from("/swagger/route2/get.yaml")
    def get(self, id='No param provided'):
        try:
            return json.dumps({id: "GET Inside route2"}), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))

    @swag_from("/swagger/route2/post.yaml")
    def post(self):
        try:
            body = request.get_json(force=True)
            body["response"] = "POST Inside route2"
            return json.dumps(body), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))
