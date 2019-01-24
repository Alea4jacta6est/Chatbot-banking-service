from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from elasticsearch import Elasticsearch
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests as rq


def get_tokens(text, analyzer="custom_analyzer"):
    host = ''
    response = rq.get(host, json={"analyzer": analyzer, "text": text})
    return list(map(lambda x: x['token'], response.json()['tokens']))


def tokens_to_term(weighted_tokens):
    prepared_tokens = []
    for token, value in weighted_tokens.items():
        prepared_token = {
            "term": {
                "text": {
                    "value": token,
                    "boost": value
                }
            }
        }
        prepared_tokens.append(prepared_token)
    return prepared_tokens


def search_by_tokens(tokens, query=None, index="sections_defs"):
    host = ''
    if query:
        body = query
    else:
        body = {
            "query": {
                "bool": {
                    "must": tokens
                }
            }
        }

    url = host + index + "/_search"
    response = rq.post(url, json=body)

    return response.json()


def get_keywords(text):
    custom_stopwords = ['A', '.', 'I', 'me', 'my', 'your', 'we']
    stop_words = stopwords.words('english') + custom_stopwords
    words = word_tokenize(text)
    keywords = [w for w in words if w not in stop_words]
    return keywords


def search_through_elastic(query):
    es = Elasticsearch(hosts='http://ec2-54-189-217-184.us-west-2.compute.amazonaws.com/')
    res = es.search(index="sections_defs", body=query)
    return res


class ActionSearchElastic(Action):

    def name(self):
        return "give_definitions_of_types_of_accounts"

    def run(self, dispatcher, tracker, domain):
        w_tokens = {}
        last_message = tracker.latest_message['text']
        for token in get_tokens(last_message):
            w_tokens[token] = 1
        prep_tokens = tokens_to_term(w_tokens)
        res = search_by_tokens(prep_tokens)
        msgs = res['hits']['hits'][0]['_source']['text']
        dispatcher.utter_message('If you are confused we can help you with additional info about types of accounts:'
                                 + msgs)
