from googleapiclient.discovery import build
import os

API_KEY = os.getenv("YOUTUBE_API_KEY", "")  # fallback key

def fetch_youtube_videos(channel_id, max_results=5):
    try:
        youtube = build("youtube", "v3", developerKey=API_KEY)

        # Get uploads playlist ID for the channel
        channel_response = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        ).execute()

        if not channel_response["items"]:
            return []

        uploads_playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        # Fetch videos from the uploads playlist
        playlist_response = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=max_results
        ).execute()

        videos = []
        for item in playlist_response.get("items", []):
            snippet = item.get("snippet", {})
            title = snippet.get("title", "No Title")
            description = snippet.get("description", "")
            publish_date = snippet.get("publishedAt", "Unknown")
            video_id = snippet.get("resourceId", {}).get("videoId", "")
            url = f"https://www.youtube.com/watch?v={video_id}" if video_id else "No URL"

            videos.append({
                "title": title,
                "description": description,
                "publish_date": publish_date,
                "url": url
            })

        return videos

    except Exception:
        return []  # Optionally: log errors to a file or Flask flash message
