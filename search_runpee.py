import requests
from bs4 import BeautifulSoup
import html5lib

def match_class(target):
    target = target.split()
    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        classes = classes.split()
        return all(c in classes for c in target)
    return do_match


class RunPeeWeb:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://covidwin.in/?state=Assam'
				#https://runpee.com/?s=
  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words

	def search(self, keywords):
		response = requests.get(self.url+keywords, headers = self.headers)
		content = response.content
		soup = BeautifulSoup(content, 'html.parser')
		result_links = soup.findAll(match_class("border bg-white shadow sm:rounded-lg mt-4 overflow-anywhere flex flex-col justify-between  mx-6 md:mx-0 self-start	min-height md:w-1/5 w-5/6"))
		shuffle(result_links)
		return result_links
      
  def send_link(self, result_links, search_words): 
    send_link = set()
    for link in result_links:
        text = link.text.lower()
        if search_words in text:  
          send_link.add(link.get('href'))
    return 
		
		#https://medium.com/codex/learn-web-scraping-the-fun-way-with-a-discord-bot-704d3422a6a2
		#https://realpython.com/beautiful-soup-web-scraper-python/
		#https://github.com/alirezamika/autoscraper
		#try and integrate twitter