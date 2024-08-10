import pytest
from my_youtube_package.data_api import fetch_video_info
import json


def load_api_key_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['api_key']

def test_fetch_video_info():
    api_token = load_api_key_from_json('/home/devansh/Documents/ytube_data_and_transcript/testing/config.json') 
    video_id = input("Enter the YouTube video ID: ")
    details = fetch_video_info(video_id, api_token)

    assert 'title' in details['snippet'], "Title not found in video snippet."
    assert 'viewCount' in details['statistics'], "View count not found in video statistics."