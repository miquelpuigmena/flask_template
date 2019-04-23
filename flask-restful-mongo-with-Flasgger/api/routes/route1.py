import json
from http import HTTPStatus
from flask import Blueprint, request, abort
from flask_restful import Resource
from logger.logger import LoggerHelper
from models.model1 import BasicModel1


class Route1(Resource):

    LOGGER = LoggerHelper.get_logger(name=__name__, filename=__name__ + ".log")

    def get(self, id='No param provided'):
        """
        Get a nice string dependant on id.
        Retrieve: GET Inside route1 - {id}.
        Parse id param and form phrase.
        If not id provided, by default id='No param provided'.
        ---
        tags:
          - Route1
        parameters:
          - in: path
            name: id
            type: string
            required: false
        produces:
          - "plain/text"
        responses:
          202:
            description: Request succeeded
          400:
            description: Internal server error
        """
        try:
            return "GET Inside route1 - " + str(id), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))

    def post(self):
        """
        Creates a new BasicModel1 and saves it!
        Query contains a Json object.
        Dummy post to create a simple model and storing in DB.
        Query must include a json data which will be returned in response with a 'response'
        field added or overwritten.
        ---
        tags:
          - Route1
        consumes:
          - application/json
        parameters:
          - in: body
            name: dummy_json
            required: true
            schema:
              type: "object"
              properties:
                dummy-field:
                  type: string
                example:
                  dummy-field: dummy-value
        responses:
          202:
            description: Post succeeded
            schema:
              type: "object"
              properties:
                dummy-field:
                  type: string
            response:
              type: string
              example:
                dummy-field: dummy-value
                response: ModelReferenced1 successfully stored
          400:
            description: Bad request
        """
        try:
            body = request.get_json(force=True)
            BasicModel1(ref_param1="uno", ref_param2="dos").save()
            body["response"] = "ModelReferenced1 successfully stored"
            return json.dumps(body), HTTPStatus.ACCEPTED
        except Exception as ex:
            abort(HTTPStatus.BAD_REQUEST, str(ex))

