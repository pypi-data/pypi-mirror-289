# import pytest:
# Imports the pytest framework, which is used for writing and running tests in Python.
# from my_youtube_package.data_api import get_video_details:
# Imports the get_video_details function from the data_api module in the my_youtube_package package. This is the function being tested.

import pytest
from my_youtube_package.data_api import get_video_details
def test_get_video_details():
    api_key = 'api_key' #replace it with a valid API key
    video_id = 'video_id' #replace it with a valid video id
    details = get_video_details(video_id, api_key)
    assert 'title' in details['snippet']
    assert 'viewCount' in details['statistics']
