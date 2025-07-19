# Influencer Monitoring Tool

This project analyzes a YouTube channel's videos by summarizing content, extracting topics, and detecting sentiment. It provides brand-friendly reports and can export the results to PDF.

## 🚀 Features

- YouTube channel analysis by channel ID
- Video summaries with sentiment and topic classification
- PDF export of all reports
- Toggleable dark mode
- Clean and professional UI

## 🛠️ Tech Stack

- Python
- Flask
- BeautifulSoup / NLP libraries
- HTML/CSS/JS

## 📦 How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2.Create and activate virtual environment:
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Run the Flask app:
python main.py

5.Visit the browser
http://127.0.0.1:5000/

📁 File Structure
your-project/
│
├── static/              # CSS/JS/Assets
├── templates/           # HTML Templates
├── main.py              # Main Flask backend
├── utils/               # NLP & YouTube utilities
├── requirements.txt     # Required Python packages
└── README.md            # Project overview and setup

📌 Notes
Ensure you have a stable internet connection for fetching YouTube data.

If using the YouTube Data API, include your API key in a .env file (if applicable).



