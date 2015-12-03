import facebook
import random
import sys
import urlparse
import threading

def status_post(token):
  messages=["Like my posts pls", "Life sucks :(", "Spinach with ice-cream <3", "Justin Beiber :*"]
  random.shuffle(messages)
  try:
    graph = facebook.GraphAPI(access_token=token)
    for m in messages: 
      graph.put_wall_post(message=m)
  except:
    print "Error posting status updates"

def post_like_and_comment(token):
  try:
    graph = facebook.GraphAPI(access_token=token)
    posts = graph.get_connections('me','posts',limit=1000)
    last=""
    post_id=""
    while 'paging' in posts and 'next' in posts['paging'] and posts['paging']['next']:
      for x in posts['data']:
        post_id=x['id']
        if(post_id==last):
          return
        last=post_id
        graph.put_comment(object_id=post_id, message='Somebody like my posts pls :(')
        graph.put_like(object_id=post_id)
      nextUrl = posts['paging']['next']
      parsed = urlparse.urlparse(nextUrl)
      until = int(urlparse.parse_qs(parsed.query)['until'][0])
      posts = graph.get_connections('me', 'posts', limit=1000, until=until)
  except:
    print "Error fetching posts"

try:
  token=sys.argv[1]
except:
  print "Access token missing"

try:
  thread1=threading.Thread(target=status_post, args=(token,))
  thread2=threading.Thread(target=post_like_and_comment, args=(token,))
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
except:
  print "Error creating threads"