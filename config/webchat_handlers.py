import tornado
from config import webchat_config
from server import webchat_login, webchat_main, webchat_registration
from webchat_api import webchat_api

api_handlers = [
    (r"/api/version", webchat_api.VersionHandler),
    (r"/api/login", webchat_api.LoginHandler),
    (r"/api/registration", webchat_api.RegistrationHandler)
]

handlers = [
    (r"/static/(.*)",  tornado.web.StaticFileHandler, {'path': "./static/app"}),
    (r"/registration", webchat_registration.RegistrationHandler),
    (r"/login", webchat_login.LoginHandler),
    (r"/", webchat_main.MainHandler)
]

handlers += api_handlers
