from working.data import (fetch_video_info)
from working.transcript import (fetch_transcript_with_lang)

def combination(video_id,api_key,lang='en'):
    video_info = fetch_video_info(video_id,api_key)
    transcript = fetch_transcript_with_lang(video_id,lang)
    return {
        'video_info':video_info,
        'transcript':transcript
    }