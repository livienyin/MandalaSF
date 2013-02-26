import argparse
import tornado.httpserver
from tornado import web

def parse_host_and_port():
        parser = argparse.ArgumentParser()
        parser.add_argument(
                '--port',
                action='store',
                type=int,
                dest='port',
                default=5000,
                help='The port that should be listned on.',
        )
        parser.add_argument(
                '--host',
                action='store',
                type=str,
                dest='host',
                default='0.0.0.0',
                help='The IP address on which to run the server.'
        )
        namespace = parser.parse_args()
        return namespace.host, namespace.port

application = web.Application(
    [
	(r"/", web.StaticFileHandler, {'path': "./static/index.html"}),
        (r"/(.*)", web.StaticFileHandler, {"path": "./static"}),
    ]
)

if __name__ == '__main__':
    host, port = parse_host_and_port()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port, address=host)
    tornado.ioloop.IOLoop.instance().start()
