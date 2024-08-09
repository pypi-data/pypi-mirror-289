from googleapiclient.discovery import build

class YouTubeDataAPI:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)
    
    def get_video_details(self, video_id):
        request = self.youtube.videos().list(part='snippet,statistics', id=video_id)
        response = request.execute()
        return response['items'][0] if 'items' in response else None
    
    def search_videos(self, query, max_results=5):
        request = self.youtube.search().list(q=query, part='snippet', type='video', maxResults=max_results)
        response = request.execute()
        return response['items'] if 'items' in response else []
    
    def list_channel_videos(self, channel_id, max_results=5):
        request = self.youtube.search().list(channelId=channel_id, part='snippet', type='video', maxResults=max_results)
        response = request.execute()
        return response['items'] if 'items' in response else []

