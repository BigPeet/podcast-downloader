#!/bin/python


from abc import ABCMeta, abstractmethod

class EpisodeFilter(object):
	__metaclass__  = ABCMeta

	@abstractmethod
	def filter_episodes(self, episodes, source):
		pass