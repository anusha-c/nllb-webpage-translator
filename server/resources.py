from flask_restful import Resource, request
import json


class Translate(Resource):
    def __init__(self):
        pass

    def post(self):
        src_lang_data = json.loads(request.data.decode())["src_lang_data"]
        # TODO: 
        #   1. Get text from HTML data
        #   2. Translate text data
        tgt_lang_data = json.loads(json.dumps({'src_lang_data': src_lang_data}))
        return tgt_lang_data
