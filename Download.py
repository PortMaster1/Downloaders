"""This is a module by Dalton Knapp
It downloads Youtube videos by
a website called Videover."""

import appex
import console
import webbrowser
import pydoc


class Download():
	def __init__(self):
		self.get()
	
	def get(self):
		try:
			url = appex.get_url()
		except:
			url = None
		finally:
			if url is None:
				appex.finish()
				console.alert("Error ???")
				exit()
			self.splitText(url)
		
	def splitText(self, url):
		text = "https://videover.com/en/downloader-online-h1?"
		#videover.com ^^^
		
		url = url.replace("https://m.youtube.com/watch?v", text, 1)
		webbrowser.open("safari-" + url)
