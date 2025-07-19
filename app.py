from flask import Flask, render_template, request
from youtube_scraper import fetch_youtube_videos
from summarizer import summarize_text
from text_analysis import analyze_sentiment, extract_topics
from trend_report import save_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        channel_id = request.form['channel_id']
        videos = fetch_youtube_videos(channel_id)
        reports = []

        for video in videos[:5]:  # Limit to top 5 videos
            if isinstance(video, dict):
                title = video.get('title', 'No Title')
                description = video.get('description', 'No Description')
                publish_date = video.get('publish_date', 'Unknown')
                url = video.get('url', 'No URL')

                full_text = f"{title}. {description}"
                summary = summarize_text(full_text)
                sentiment = analyze_sentiment(description)
                topics = extract_topics(full_text)

                reports.append({
                    "title": title,
                    "publish_date": publish_date,
                    "url": url,
                    "summary": summary,
                    "sentiment": sentiment,
                    "topics": topics
                })

        save_report(reports)
        return render_template("index.html", reports=reports)

    return render_template("index.html", reports=None)

if __name__ == '__main__':
    app.run(debug=True)
