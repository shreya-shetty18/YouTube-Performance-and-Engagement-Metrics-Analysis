# 📊 YouTube Performance and Engagement Metrics Analysis

This project analyzes the top 20 trending YouTube channels in a user-specified category using the YouTube Data API. It retrieves key performance and engagement metrics such as views, likes, comments, and subscriber counts, then visualizes insights through a Tableau dashboard.

---

## 🚀 Overview

The goal of this project is to:
- Identify the top 20 high-performing YouTube channels in a given category.
- Scrape video-level and channel-level metrics using the YouTube Data API.
- Analyze engagement and influence patterns across these channels.
- Visualize insights using a comprehensive Tableau dashboard.
  
---

## 🧪 Features

### ✅ Data Collection:
- Fetches the **top 20 trending YouTube channels** in a given category.
- Extracts:
  - Top 50 videos per channel (by view count)
  - Views, Likes, Comments
  - Subscriber counts & video counts (channel level)

### ✅ Data Processing:
- Combines video-level and channel-level metrics into a clean dataset.
- Saves the final merged dataset as a `.csv` file.

### ✅ Visualization:
- Tableau dashboard presents:
  - Most viewed videos across channels
  - Engagement metrics per channel
  - Comparison of subscriber counts vs average video views
  - Channel influence and performance benchmarking

---

## 🔧 Requirements

- Python 3.x
- Google API Client
- Pandas
- Tableau (for visualization)

---

## 📊 Tableau Dashboard Overview
The Tableau dashboard visualizes key engagement metrics and channel comparisons:

1. Top 10 Videos by Views
Highlights content that drives massive traffic.

2. Likes vs Comments Scatter Plot
Reveals the correlation between likes and viewer interaction.

3. Subscribers vs Total Video Count
Helps assess if channel size impacts publishing frequency.

4. Channel Engagement Matrix
Compares views, likes, and comments across top 20 channels.

5. Filters by Channel and Metric
Interactively explore performance of specific channels.

---

## Sample Output Columns
title	views	likes	comments	channel_id	channel_title	subscriber_count	video_count
AI Trends 2024	1.2M	32K	980	UC1234	FutureTechDaily	1.5M	340
DIY Drone Build	850K	15K	410	UC5678	MakerZone	950K	190

---

## 💡 Use Cases
✔️ For Influencer Marketing Teams

Identify which creators have the highest engagement per viewer.

Track competitors and benchmark channel performance.

✔️ For Content Strategists

Understand which video types are most effective.

Determine the best mix of frequency, content style, and length.

✔️ For Analysts & Data Enthusiasts

Apply data science techniques on real-world social data.

Experiment with new metrics like engagement ratio, comment-to-like ratio, etc.

---

## 🧠 Key Insights from Analysis

📍 Based on a test run using a sample category (e.g., **Technology**), here are key findings:

- **High engagement doesn’t always correlate with high subscriber counts.**
  - Some niche channels with fewer subscribers often show better engagement rates (likes/comments per view).

- **Top 10 videos account for more than 60% of total views across channels.**
  - Suggests power law distribution in content popularity.

- **Channels with consistent video publishing (higher video count) tend to have broader reach**, but engagement per video may drop slightly with volume.

- **Certain videos went viral primarily due to timing and keyword trends**, not just channel popularity.

- **Subscriber count is a weak predictor of video likes.** Viewer interaction relies more on content quality and topic relevance.

---

## ✨ Enhancements for Future
Add sentiment analysis on comments.

Include video duration and publish date as features.

Develop engagement score metric.

Automate trend detection using keyword tracking.



