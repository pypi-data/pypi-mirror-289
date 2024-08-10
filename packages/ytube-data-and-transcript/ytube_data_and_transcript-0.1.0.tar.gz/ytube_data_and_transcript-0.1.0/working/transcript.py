from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def fetch_transcript(video_id, lang='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, [lang])
        formatted_transcript = "\n".join([line['text'] for line in transcript])
        return formatted_transcript
    except NoTranscriptFound:
        raise RuntimeError(f"No transcript found for language '{lang}' in video {video_id}.")
    except TranscriptsDisabled:
        raise RuntimeError(f"Transcripts are disabled for the video {video_id}.")
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {e}")
    
def fetch_transcript_with_lang(video_id, lang='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, [lang])
        formatted_transcript = "\n".join([line['text'] for line in transcript])
        return formatted_transcript
    except Exception as e:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en'])
            formatted_transcript = "\n".join([line['text'] for line in transcript])
            return formatted_transcript
        except Exception as fallback_e:
            raise RuntimeError(f"Error fetching transcript: {e}\nFallback attempt failed: {fallback_e}")

def is_transcript_available(video_id, lang='en'):
    try:
        YouTubeTranscriptApi.get_transcript(video_id, [lang])
        return True
    except:
        return False