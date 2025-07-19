from datetime import datetime

def save_report(video_reports):
    filename = f"trend_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("📰 Influencer Trend Summary Report\n")
        f.write("=" * 40 + "\n\n")

        for idx, report in enumerate(video_reports, 1):
            f.write(f"📌 Video {idx}\n")
            f.write(f"🎥 Title: {report['title']}\n")
            f.write(f"🗓️ Published On: {report['publish_date']}\n")
            f.write(f"🔗 URL: {report['url']}\n\n")
            f.write(f"📝 Summary:\n{report['summary']}\n\n")
            f.write(f"📚 Topics: {', '.join(report['topics'])}\n")
            f.write(f"💬 Sentiment: {report['sentiment']}\n")
            f.write("-" * 40 + "\n\n")

    print(f"✅ Report saved as {filename}")
