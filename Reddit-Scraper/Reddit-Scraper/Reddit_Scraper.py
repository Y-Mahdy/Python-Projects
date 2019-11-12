import praw
import ctypes
import sys
import datetime

def main(threshold,startpoint,limit,days):
    reddit = praw.Reddit(client_id = 'Kq82_2WoBaP2fQ', 
                         client_secret = 'iEUL8J7N8BFBamcX2k440-Sj1hw',
                         username = 'mennatullah-sobhy',
                         password = 'PWDreddit@1234',
                         user_agent = 'reddit-posts')
    try:
        fresults = open('comments.txt', 'r')
    except IOError:
        fresults = open('comments.txt', 'w')
    while True:
        try:
            subreddit = reddit.subreddit(startpoint)
            hot_python = subreddit.hot(limit = None)
            count =0
            countcommnt =0
            for submission in hot_python:
                count= count +1
                try:
                    print('Submission ' +str(count) + ': ' + submission.title)
                    submission.comments.replace_more(limit = 0)
                    for top_level_comment in submission.comments:
                        try:
                            date = int(top_level_comment.created)
                            now = int(datetime.datetime.timestamp(datetime.datetime.now()))
                            if (date > now):
                                delta = date - now
                            else:
                                delta = now - date
                            PostHours = delta/3600
                            if countcommnt <= limit:
                                if (PostHours <= 24 * days):
                                    if top_level_comment.score >= threshold:
                                        countcommnt = countcommnt + 1
                                        comment = 'Comment ' +str(countcommnt) +' >> '+ str(top_level_comment.score) + ' : ' + top_level_comment.body
                                        print(comment)
                                        file = open('comments.txt','a') 
                                        file.write(str(comment.encode('utf8')) + '\n')
                                        file.close()
                            else:
                                break
                        except Exception as e:
                                print (str(e))
                except Exception as e:
                    logger.error('Error '+ str(e))
                if countcommnt > limit:
                    break
            break
        except Exception as e:
            if count is 0:
                print('Error: ' + str(e))
                startpoint = input ('<sub-reddit>: ') 
if __name__ == "__main__":
    try:
        tempa = sys.argv[1]
    except:
        tempa = input ('<threshold>: ')
    try:
         b = sys.argv[2]
    except:
         b = input ('<sub-reddit>: ')
    try:
        tempc = sys.argv[3]
    except:
        tempc = input ('<Comments'' Limit>: ')
    try:
        tempd = sys.argv[4]
    except:
        tempd = input ('<Past Days>: ')
    while True:
        try:
            a = int(tempa)
            break
        except:
            tempa = input('Please insert <threshold> integer number')
    while True:
        try:
            c = int(tempc)
            break
        except:
            tempc = input('Please insert <limit> integer number')
    while True:
        try:
            d = int(tempd)
            break
        except:
            tempd = input('Please insert <past days> integer number')
    main(a, b, c, d)