import tornado.ioloop
import tornado.web

from config import webchat_config, webchat_handlers


def make_app():
    return tornado.web.Application(webchat_handlers.handlers, "", None, **webchat_config.settings)
if __name__ == "__main__":
    app = make_app()
    app.listen(webchat_config.port)
    tornado.ioloop.IOLoop.current().start()
