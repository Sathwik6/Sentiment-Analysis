from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import importlib.util
import os

# Construct the absolute path to config.py
# __file__ is a special variable that holds the path to the current script. 
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../youtube_sentiment_analysis', 'config.py'))
spec = importlib.util.spec_from_file_location("config", config_path)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

YOUTUBE_API_KEY = config.YOUTUBE_API_KEY


def fetch_comments(video_id, numComments):
    # Build the service object for the YouTube API
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    comments = []
    try:
        # Make the API call to get the top-level comment threads
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults= min(numComments, 1000),
            textFormat='plainText'
        )
        response = request.execute()

        # Loop through each comment thread
        for item in response['items']:
            # Extract the top-level comment from each thread
            top_level_comment = item['snippet']['topLevelComment']
            comment_text = top_level_comment['snippet']['textDisplay']
            comments.append(comment_text)
            
            # If you also want to fetch replies in each thread, you can do so here
            
    except HttpError as e:
        print(f"An HTTP error occurred: {e.resp.status} {e.content}")
    except KeyError as e:
        print(f"A KeyError occurred: {e}")

    return comments
