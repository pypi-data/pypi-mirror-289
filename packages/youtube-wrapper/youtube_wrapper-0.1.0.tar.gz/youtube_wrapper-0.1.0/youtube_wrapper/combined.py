from .data_api import YouTubeDataAPI
from .transcript_api import YouTubeTranscriptAPI

class YouTubeWrapper:
    def __init__(self, api_key):
        self.data_api = YouTubeDataAPI(api_key)
        self.transcript_api = YouTubeTranscriptAPI()
    
    def get_video_info_and_transcript(self, video_id):
        video_details = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.get_transcript(video_id)
        return {
            'video_details': video_details,
            'transcript': transcript
        }

