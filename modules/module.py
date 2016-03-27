#!/bin/python

from sources.source import YOUTUBE_PLAYLIST
from youtube import yt_scanner, yt_downloader, yt_filter
from abc import ABCMeta, abstractmethod

class Module:
	__metaclass__  = ABCMeta

	def __init__(self, scanner, downloader, episode_filter):
		self.scanner = scanner
		self.downloader = downloader
		self.episode_filter = episode_filter


	def scan(self, source):
		""" Returns a list with all episodes from this source """
		return self.scanner.scan(source)

	def download_episodes(self, episodes):
		for episode in episodes:
			self.downloader.download(episode)

	def filter_episodes(self, episodes, source):
		return self.episode_filter.filter_episodes(episodes, source)

	@staticmethod
	def create_module(source_type):
		if source_type == YOUTUBE_PLAYLIST:
			return YoutubePlaylistModule()
		else:
			raise NotImplementedError


class YoutubePlaylistModule(Module):

	def __init__(self):
		Module.__init__(self, yt_scanner.YoutubePlaylistScanner(), 
			yt_downloader.YoutubePlaylistDownloader(), 
			yt_filter.YoutubePlaylistFilter())


