import json
from http import HTTPStatus
from flask import Blueprint, request, abort
from flask_restful import Resource
from logger.logger import LoggerHelper


class Route2(Resource):

    LOGGER = LoggerHelper.get_logger(name=__name__, filename=__name__ + ".log")

    def get(self, id='No param provided'):
        """
        GET method

        :return: String
        """
        return "GET Inside route2 - " + str(id)

    def post(self):
        """
            POST method

            :return: Json
            :raises:
                - HTTP
            """
        try:
            body = request.get_json(force=True)
            body["response"] = "POST Inside route2"
            return json.dumps(body), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))
