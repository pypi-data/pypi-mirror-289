from googleapiclient.discovery import build

def initialize_service(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def fetch_channel_videos(channel_id,api_key,max_res=10):
    service = initialize_service(api_key)
    request = service.search().list(
        part='snippet',
        channelId=channel_id,
        results=max_res,
        order='date'
    )
    response = request.execute()
    return response['items']    # return the list of items

def fetch_video_info(video_identifier, api_key):
    service = initialize_service(api_key)
    request = service.videos().list(
        part='snippet,statistics',
        id=video_identifier
    )
    response = request.execute()
    
    if not response['items']:
        raise ValueError(f"No video found with the provided video ID: {video_identifier}")
    
    return response['items'][0]  # return the first item in the list
# return the first item in the list

def search_to_fetch_videos(search_query,api_key,max_res=10):
    service = initialize_service(api_key)
    request = service.search().list(
        q=search_query,
        part='snippet',
        type='video',
        results=max_res
    )
    response = request.execute()
    return response['items']    # return the list of items



