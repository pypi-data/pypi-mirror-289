import pytest
from working.transcript import fetch_transcript

def test_fetch_transcript():
    video_id = input("Enter the YouTube video ID: ")
    transcript = fetch_transcript(video_id)
    
    assert isinstance(transcript, str), "Transcript is not a string."
    assert len(transcript) > 0, "Transcript is empty."

