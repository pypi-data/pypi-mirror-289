# import pytest:
# Imports the pytest framework, which is used for writing and running tests in Python.
# from my_youtube_package.combined_api import get_video_info_with_transcript:
# Imports the get_video_info_with_transcript function from the combined_api module in the my_youtube_package package. This is the function being tested.
# from unittest.mock import patch:
# Imports the patch decorator from unittest.mock to mock dependencies in the tests.

import pytest
from my_youtube_package.combined_api import get_video_info_with_transcript
from unittest.mock import patch

# Sample data for mocking
sample_video_details = {
    'snippet': {
        'title': 'Sample Video Title',
        'description': 'Sample Video Description',
    },
    'statistics': {
        'viewCount': '1000',
        'likeCount': '100',
    }
}

sample_transcript = "This is a sample transcript."

# Mock the get_video_details and get_transcript_with_translation functions
@patch('my_youtube_package.combined_api.get_video_details')
@patch('my_youtube_package.combined_api.get_transcript_with_translation')
def test_get_video_info_with_transcript(mock_get_transcript, mock_get_video_details):
    # Define the behavior of mocks
    mock_get_video_details.return_value = sample_video_details
    mock_get_transcript.return_value = sample_transcript
    
    api_key = 'test_api_key'
    video_id = 'test_video_id'
    language = 'en'
    
    result = get_video_info_with_transcript(video_id, api_key, language)
    
    # Assertions to verify correct behavior
    assert result['video_details'] == sample_video_details
    assert result['transcript'] == sample_transcript

    mock_get_video_details.assert_called_once_with(video_id, api_key)
    mock_get_transcript.assert_called_once_with(video_id, language)

# Additional test case for error handling
@patch('my_youtube_package.combined_api.get_video_details')
@patch('my_youtube_package.combined_api.get_transcript_with_translation')
def test_get_video_info_with_transcript_error(mock_get_transcript, mock_get_video_details):
    # Make get_video_details raise an exception to test error handling
    mock_get_video_details.side_effect = Exception("API Error")
    mock_get_transcript.return_value = sample_transcript
    
    api_key = 'test_api_key'
    video_id = 'test_video_id'
    language = 'en'
    
    with pytest.raises(Exception):
        get_video_info_with_transcript(video_id, api_key, language)
