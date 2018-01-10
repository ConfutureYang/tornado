#coding:utf-8
from tornado import ioloop
from tornado  import web
import time

class MainHandler(web.RequestHandler):
	def get(self):
		print self.get_argument("y")
		self.write("Hello Tornado")

def make_app():
	return web.Application([(r"/",MainHandler),])


if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	ioloop.IOLoop.current().start()