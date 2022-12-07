from flask_restful import Resource, request
from bs4 import BeautifulSoup
import requests
import json


class Translate(Resource):
    def __init__(self):
        pass

    def post(self):
        src_url = json.loads(request.data.decode())["src_url"]
        # TODO: 
        #   1. Get text from HTML data
        #   2. Translate text data
        page = requests.get(src_url)
        parsedPage = BeautifulSoup(page.content, "html.parser")
        print(parsedPage)
        tgt_lang_data = json.loads(json.dumps({'src_lang_data': src_url}))
        return tgt_lang_data
