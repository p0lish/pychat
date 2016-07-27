from datetime import date

import tornado.log as log
import tornado.web

from config import webchat_config


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = {'version': webchat_config.api_version,
                    'last_build': date.today().isoformat()
                    }
        self.write(response)

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear();
        self.set_status(403)
        self.finish("")


    def post(self):
        response = self.get_argument('username')
        log.app_log.info(response)
        self.write(response)


class RegistrationHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear()
        self.set_status(403)
        self.finish("")

    def post(self):
        self.clear()
        self.set_status(404)


