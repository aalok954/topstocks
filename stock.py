import random
import string

import redis
import cherrypy
r = redis.Redis(host='localhost',port=6379,db=0)

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
	r = redis.StrictRedis()
	with open(file_name, 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
	r.zadd("search",row['SC_NAME'] = row['HIGH'])
        return 'r.zrevrange("search",1,10,WITHSCORES)'+"""<html>
          <head>
	   <link href="/static/css/style.css" rel="stylesheet">
	  </head>
          <body>
	<div id="search">
	<h3>Search</h3>
            <form method="post" action="generate">
              <input type="text" name="search_name" />
              <button type="submit">Search</button>
            </form>
     </body>
</html>"""
    
        

    @cherrypy.expose
    def generate(self, search_name):
        return ''.r.get("search_name")


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())