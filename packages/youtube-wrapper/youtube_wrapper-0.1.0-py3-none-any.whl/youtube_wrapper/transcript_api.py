import requests

class YouTubeTranscriptAPI:
    def __init__(self):
        self.api_url = 'https://www.googleapis.com/youtube/v3/captions'
    
    def get_transcript(self, video_id):
        response = requests.get(f'{self.api_url}/{video_id}/transcript')
        if response.status_code == 200:
            return response.json()
        else:
            return None

