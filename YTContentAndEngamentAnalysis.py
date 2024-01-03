import pandas as pd
from googleapiclient.discovery import build


def video_content_analysis(youtube, channel_ids):
    """
    This function performs Video Content and Influencer Network Analysis for each channel
    :params: YouTube: YouTube Object
    :params: channel_ids: Top 20 channel Ids
    :returns: CSV file
    """
    combined_data = []

    for competitor_id in channel_ids:
        channel_data = {}

        # Performing Video Content Analysis for each channel
        video_content_data = []

        video_request = youtube.search().list(
            part="snippet",
            channelId=competitor_id,
            type="video",
            order="viewCount",
            maxResults=50
        )
        video_response = video_request.execute()
        video_id = [item["id"]["videoId"]for item in video_response["items"]]
        video_id = ','.join(video_id)
        video_stat_request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            maxResults=50,
            id=video_id
        )
        video_stat_response = video_stat_request.execute()
        for video in video_stat_response.get("items", []):
            video_info = {
                "title": video["snippet"].get("title"),
                "views": video["statistics"].get("viewCount"),
                "likes": video["statistics"].get("likeCount",0),
                "comments": video["statistics"].get("commentCount",0),
                "channel_id": competitor_id
            }
            video_content_data.append(video_info)

        channel_data['video_content_data'] = video_content_data

        # Performing Influencer Network Analysis for each channel
        influencer_network_data = []
        request = youtube.channels().list(
            part="snippet,statistics",
            id=competitor_id
        )
        response = request.execute()
        for channel in response.get("items", []):
            channel_info = {
                "channel_title": channel["snippet"]["title"],
                "subscriber_count": channel["statistics"]["subscriberCount"],
                "video_count": channel["statistics"]["videoCount"],
                "channel_id": competitor_id
            }
            influencer_network_data.append(channel_info)
        channel_data['influencer_network_data'] = influencer_network_data
        combined_data.append(channel_data)
    video_content_df = pd.DataFrame(sum((d['video_content_data'] for d in combined_data), []))
    influencer_network_df = pd.DataFrame(sum((d['influencer_network_data'] for d in combined_data), []))

    # Merging the two datasets on 'channel_id'
    combined_df = pd.merge(video_content_df, influencer_network_df, on='channel_id')

    # Saving the data to a CSV file
    combined_df.to_csv('YouTube Scraped data.csv', index=False)


def find_top_unique_channels_for_category(youtube, category):
    """
    This function uses YouTube API and finds 20 top channel titles for the given category.
    :params: YouTube: YouTube Object
    :params: category: Input category
    """
    channel_names = set()
    top_20_channels = []

    # filtering the search according to the requirement
    request = youtube.search().list(
        part="snippet",
        q=category,
        type="channel",
        maxResults=50,
        order="viewCount"
    )
    response = request.execute()
    for channel in response.get("items", []):
        channel_id = channel["snippet"]["channelId"]
        channel_title = channel["snippet"]["title"]
        if channel_title not in channel_names:
            top_20_channels.append({"channel_id": channel_id, "channel_title": channel_title})
            channel_names.add(channel_title)
            if len(top_20_channels) >= 20:
                break

    for channel in top_20_channels:
        print(channel["channel_title"])
    channel_ids = [channel['channel_id'] for channel in top_20_channels]

    # calling this function to analyze the videos of top 20 channels and perform influencer network analysis
    video_content_analysis(youtube, channel_ids)


if __name__ == '__main__':
    # Find top unique channels in YouTube for the given category
    category = input("Enter the category for which you would like to see the top 20 trending channels on YouTube.")
    api_key = '' # enter your API Key
    api_service_name = "youtube"
    api_version = "v3"
    youtube_obj = build(api_service_name, api_version, developerKey=api_key)
    find_top_unique_channels_for_category(youtube_obj,category)


