#!/usr/bin/python

from modules.scanner import Scanner
from modules.episode import Episode
from config_parser import parse_config
from apiclient.discovery import build
import logging
import os.path


CUR_DIR = os.path.dirname(__file__)
CONFIG_FILE = CUR_DIR + "/../../conf/modules/youtube/youtube_api.conf"

class YoutubePlaylistScanner(Scanner):

	def __init__(self):
		self.config = parse_config(CONFIG_FILE)

	def scan(self, source):
		episodes = []
		service_name = self.config["YOUTUBE_API_SERVICE_NAME"]
		api_version = self.config["YOUTUBE_API_VERSION"]
		key = self.config["YOUTUBE_API_DEVELOPER_KEY"]
		youtube = build(service_name, api_version, developerKey=key)

		# Retrieve the list of videos uploaded to the authenticated user's channel.
  		playlistitems_list_request = youtube.playlistItems().list(
  			playlistId=source.id,
  			part="snippet",
  			maxResults=50)

  		#while playlistitems_list_request:
  		playlistitems_list_response = playlistitems_list_request.execute()

  			# Print information about each video.
  		for playlist_item in playlistitems_list_response["items"]:
  			title = playlist_item["snippet"]["title"]
  			video_id = playlist_item["snippet"]["resourceId"]["videoId"]
  			timestamp = playlist_item["snippet"]["publishedAt"]

  			logging.debug("%s (%s) [%s]" % (title, video_id, timestamp))

  			episodes.append(Episode(source, video_id, title, timestamp))

  		return episodes


