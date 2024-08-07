from googleapiclient.discovery import build  #Imports the build function from the googleapiclient.discovery module, which is used to construct a service object for interacting with the API.

def get_service(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id, api_key):
    service = get_service(api_key)
    request = service.videos().list(
        part="snippet,statistics", #Specifies part="snippet,statistics" to get both the snippet (metadata like title, description) and statistics (view count, like count, etc.) of the video.
        id=video_id
    )
    response = request.execute()
    return response['items'][0]

def search_videos(query, api_key, max_result=5):
    service = get_service(api_key)
    request = service.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResult=max_result
    )
    response = request.execute()
    return response['items']

def list_channel_videos(channel_id, api_key, max_results=5):
    service = get_service(api_key)
    request = service.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        order="date"
    )
    response = request.execute()
    return response['items']


