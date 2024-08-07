# from my_youtube_package.transcript_api import get_transcript:
# Imports the get_transcript function from the transcript_api module in the my_youtube_package package. This is the function being tested.

import pytest
from my_youtube_package.transcript_api import get_transcript

def test_get_transcript():
    video_id = 'video_id' #replace it with a valid video id
    try:
        transcript = get_transcript(video_id)
        assert isinstance(transcript, str)
        assert len(transcript) > 0
    except RuntimeError as e:
        pytest.fail(f"Test failed: {e}")