# from .data_api import get_video_details, search_videos, list_channel_videos:
# This imports three functions (get_video_details, search_videos, list_channel_videos) from a module named data_api located in the same package (denoted by the .). These functions are likely used to interact with YouTube Data API.
# from .transcript_api import get_transcript, get_transcript_with_translation, transcript_available:
# This imports three functions (get_transcript, get_transcript_with_translation, transcript_available) from a module named transcript_api in the same package. These functions are likely used to interact with YouTube transcript API.

from .data_api import get_video_details, search_videos, list_channel_videos
from .transcript_api import get_transcript, get_transcript_with_translation, transcript_availabe

def get_video_info_with_transcript(video_id, api_key, language='en'):
    video_details = get_video_details(video_id,api_key)
    transcript = get_transcript_with_translation(video_id, language)
    return{
        'video_details': video_details,
        'transcript': transcript
    }