from flask_restful import Resource, request
from bs4 import BeautifulSoup
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import requests
import json


class Translate(Resource):
    def __init__(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
        
        self.translator = pipeline('translation', model=self.model, tokenizer=self.tokenizer, src_lang="eng_Latn", tgt_lang=
                     "mai_Deva")

    def post(self):
        src_url = json.loads(request.data.decode())["src_url"]
        # TODO: 
        #   1. Get text from HTML data
        #   2. Translate text data
        page = requests.get(src_url)
        parsedPage = BeautifulSoup(page.content, "html.parser")
        print("translating...")
        print(self.translator(parsedPage))
        tgt_lang_data = json.loads(json.dumps({'src_lang_data': src_url}))
        return tgt_lang_data
