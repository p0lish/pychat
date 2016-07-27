import tornado.web
class RegistrationHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("registration/registration.html")
