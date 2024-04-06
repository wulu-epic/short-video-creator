import praw, os
from dotenv import load_dotenv

class RScraper(object):
    def __init__(self) -> None:
        self.dotenv_path = "C:/Users/Martin/Documents/Python Projects/main-projects/shorts_video_auto_creator/.env"
        load_dotenv(dotenv_path=self.dotenv_path)

        self.secret = os.getenv('SECRET')
        self.personal_use = os.getenv('PERSONAL_USE')
        self.redirect_uri = 'http://localhost:8080'
        self.authorization_token = ''
    
    def prompt_auth_token(self):
        pass
    
    def scrape(self, subreddit: str, *args):
        reddit_read_only = praw.Reddit(client_id=self.personal_use, client_secret=self.secret, user_agent="short_maker2/0.0.1")
        subreddits = [subreddit] if subreddit else []
        subreddits += [arg for arg in args]

        posts = {}

        for sub_reddit in subreddits:
            sbreddit = reddit_read_only.subreddit(sub_reddit)
            posts[sub_reddit] = []

            for post in sbreddit.top(limit=2):
                posts[sub_reddit].append({'title': post.title, 'text': post.selftext})

        return posts
    
    def get_post_title(self, post : dict) -> str:
        return post.get('title')
    
    def get_post_text(self, post : dict) -> str:
        return post.get('text')