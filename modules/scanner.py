#!/bin/python


from abc import ABCMeta, abstractmethod

class Scanner(object):
	__metaclass__  = ABCMeta

	@abstractmethod
	def scan(self, source):
		pass