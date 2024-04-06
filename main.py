from libraries.reddit_scraper import rscraper
from libraries.voice_ai import voice
from libraries.speak_posts import post_speaker as speaker

class Main(object):
    def __init__(self):
        self.scraper = rscraper.RScraper()
        self.voice = voice.Voice()

        self.SAVE_DIRECTORY = "C:/Users/Martin/Documents/Python Projects/main-projects/shorts_video_auto_creator/"

    def run(self):
        posts = self.scraper.scrape("shortstories")
        if not posts:
            print('[-] Failed to gather posts please try again later')
            return
        
        print(f'[+] Gathered {len(posts.items())} posts.')
        
        post_speaker = speaker.PostSpeaker(posts, self.voice, self.scraper)
        post_speaker.speak_all_posts()

if __name__ == '__main__':
    main = Main()
    main.run()