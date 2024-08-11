from .data_api import YouTubeDataAPI
from .transcript_api import YouTubeTranscriptWrapper

class YouTubeWrapper:
    def __init__(self, api_key):
        self.data_api = YouTubeDataAPI(api_key)
        self.transcript_api = YouTubeTranscriptWrapper()

    def get_video_data_with_transcript(self, video_id, language='en'):
        video_data = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.get_transcript(video_id, language)
        return {
            'video_data': video_data,
            'transcript': transcript
        }
