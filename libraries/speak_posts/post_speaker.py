from libraries.reddit_scraper import rscraper
from libraries.voice_ai import voice
from libraries.reddit_scraper import rscraper as scraper
from libraries.utilities import utilities

from threading import Thread, Lock

class PostSpeaker(object):
    def __init__(self, posts, _voice : voice.Voice, rscraper : scraper.RScraper):
        self.posts : dict = posts
        self.voice : voice.Voice = _voice
        self.rscraper : scraper.RScraper = rscraper
        self.utilities : utilities.Utilities = utilities.Utilities()

        self.lock = Lock()
        self.threads = []

    def speak_post(self, post):
        title, text = self.utilities.text_edge_cases(self.rscraper.get_post_title(post)), self.rscraper.get_post_text(post)
        
        self.voice.say(text, f"{title}.mp3")
        print(f'[+] Speaked "{title}" successfully. Saved in desired location.')

        if self.lock.locked():
            self.lock.release()


    def speak_all_posts(self):
        # TODO: This will only access the first sub reddit! Do not forget to make this properly functional!
        all_posts : list[dict] = list(self.posts.items())[0][1]

        self.lock.acquire()
        for post in all_posts:
            thread = Thread(target=self.speak_post, args=(post, ))
            thread.start()
            self.threads.append(thread)

        self.utilities.clean_threads(self.threads)

        if self.lock.locked():
            self.lock.release()
        
        
