#!/usr/bin/python

import argparse
from sources import sourcelist_parser

class PodcastDownloader():
	def __init__(self, source_list_file):
		self.sources = sourcelist_parser.parse_sources(source_list_file)
		self.loaded_modules = {}

	def check_sources(self):
		for source in self.sources:
			source_module = self.load_module(source.type)

	def download_episode(self):
		pass

	def load_module(self, source_type):
		if source_type in self.loaded_modules.keys():
			return self.loaded_modules[source_type]
		else:
			module = self.create_module(source_type)
			self.loaded_modules[source_type] = module
			return module

	def create_module(self, source_type):
		return None


if __name__ == "__main__":

  parser = argparse.ArgumentParser("Text")

  parser.add_argument("--loop", default=None, help="The frequency the sources will be checked with. \
  	If no value is specified, the sources will be checked only once.")
  parser.add_argument("--sources", default="conf/sources.list", help="path to the list of podcast sources")

  args = parser.parse_args()

  downloader = PodcastDownloader(args.sources)
  downloader.check_sources()

  	
