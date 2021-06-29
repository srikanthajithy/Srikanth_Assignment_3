from timer import Timer
from reader import feed


def Cal():
    """Print the 10 latest tutorials from Real Python"""
    t = Timer(text="Downloaded 10 tutorials in {:0.2f} seconds")
    t.start()
    for tutorial_num in range(10):
        tutorial = feed.get_article(tutorial_num)
        print(tutorial)
    t.stop()

