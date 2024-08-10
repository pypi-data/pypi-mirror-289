import pytest
from working.mix import combination
from unittest.mock import patch

sample_vid_info = {
    'snippet': {
        'title': 'Video Title example',
        'description': 'Video Description',
    },
    'statistics': {
        'viewCount': '5000',
        'likeCount': '450',
    }
}

sample_transcript = "This is a sample."

@patch('working.transcript.fetch_transcript_with_lang')
@patch('working.data.fetch_video_info')
def test_get_video_info_with_transcript(mock_fetch_video_info, mock_fetch_transcript_with_lang):

    mock_fetch_video_info.return_value = sample_vid_info
    mock_fetch_transcript_with_lang.return_value = sample_transcript
    
    api_key = 'test_api_key'
    video_id = 'test_video_id'
    language = 'en'
    
    result = combination(video_id, api_key, language)
    assert result['video_info'] == sample_vid_info
    assert result['transcript'] == sample_transcript

    mock_fetch_video_info.assert_called_once_with(video_id, api_key)
    mock_fetch_transcript_with_lang.assert_called_once_with(video_id, language)

@patch('working.transcript.fetch_transcript_with_lang')
@patch('working.data.fetch_video_info')
def test_get_video_info_with_transcript_error(mock_fetch_video_info, mock_fetch_transcript_with_lang):
    mock_fetch_video_info.side_effect = Exception("API Error")
    mock_fetch_transcript_with_lang.return_value = sample_transcript
    
    api_key = 'test_api_key'
    video_id = 'test_video_id'
    language = 'en'
    
    with pytest.raises(Exception):
        combination(video_id, api_key, language)