import os
from dotenv import load_dotenv
import praw
from concurrent.futures import ProcessPoolExecutor
from imageDownloader import downloadFile

load_dotenv()
username = os.getenv("USERNAME")
reddit = praw.Reddit(
    client_id=os.getenv("CLIENTID"),
    client_secret=os.getenv("SECRET"),
    user_agent=f"scraper/1.0 by {username}",
)


def multiThreadedDownloadCall(imageList):
    # length = len(imageList)
    with ProcessPoolExecutor() as excutor:
        # for length  in excutor.map(downloadFile,imageList)
        excutor.map(downloadFile, imageList)


def getRedditImageURL(subredditName="ProgrammerHumor"):
    imageList = []
    for submission in reddit.subreddit(f"{subredditName}").hot(limit=10):
        imageList.append(submission.url)
    return imageList


imageURLlist = getRedditImageURL()
multiThreadedDownloadCall(imageURLlist)
