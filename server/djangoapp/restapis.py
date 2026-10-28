import os

import requests
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv("backend_url", "").rstrip("/")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url",
    "",
).rstrip("/") + "/"


def get_request(endpoint, **kwargs):
    request_url = f"{backend_url}/{endpoint.lstrip('/')}"
    try:
        response = requests.get(request_url, params=kwargs, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"GET request failed: {err}")
        return None


def analyze_review_sentiments(text):
    if not sentiment_analyzer_url:
        print("Sentiment analyzer URL is not configured.")
        return None

    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Sentiment request failed: {err}")
        return None


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Review request failed: {err}")
        return None