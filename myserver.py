#coding:utf-8
from tornado import ioloop
from tornado  import web
import time
import json

class MainHandler(web.RequestHandler):
	def get(self):
		y = self.get_argument("y")
		print y
		self.write("Hello Tornado")

def make_app():
	return web.Application([(r"/",MainHandler),])


if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	ioloop.IOLoop.current().start()
