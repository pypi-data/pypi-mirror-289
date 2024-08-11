from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

class YouTubeTranscriptWrapper:
    def get_transcript(self, video_id, language='en'):
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        formatter = JSONFormatter()
        return formatter.format_transcript(transcript)

    def list_transcripts(self, video_id):
        return YouTubeTranscriptApi.list_transcripts(video_id)
