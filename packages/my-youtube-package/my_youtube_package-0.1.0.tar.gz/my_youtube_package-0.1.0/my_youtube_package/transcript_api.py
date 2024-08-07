# Imports YouTubeTranscriptApi from the youtube_transcript_api module to interact with YouTube's transcript API.
# Imports TextFormatter to format the transcript into a readable text format.

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id, languages=['en']):                                 
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages)
        formatter = TextFormatter()                                             
        return formatter.format_transcript(transcript)
    except Exception as e:
        raise RuntimeError(f"Error retrieving transcript: {e}")

def get_transcript_with_translation(video_id, language='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, [language])
    except:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en'])
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

def transcript_availabe(video_id):
    try:
        YouTubeTranscriptApi.get_transcript(video_id)
        return True
    except:
        return False

# eg
# video_id = 'XXYlFuWEuKI'
# print(get_transcript(video_id))
