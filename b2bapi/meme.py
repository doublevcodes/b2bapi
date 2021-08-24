class Meme:
    __slots__ = ("title", "url", "link", "subreddit")

    def __init__(self, title: str, url: str, link: str, subreddit: str) -> None:
        self.title = title
        self.url = url
        self.link = link
        self.subreddit = subreddit