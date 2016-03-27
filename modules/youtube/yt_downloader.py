from modules.downloader import Downloader
import logging

class YoutubePlaylistDownloader(Downloader):

	def download(self, episode):
		logging.debug(episode)

