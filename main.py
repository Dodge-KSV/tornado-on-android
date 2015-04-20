# install_twisted_rector must be called before importing  and using the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()

from tornado.platform.twisted import TwistedIOLoop
from twisted.internet import reactor
TwistedIOLoop().install()
# Set up your tornado application as usual using `IOLoop.instance`

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

from kivy.app import App
from kivy.uix.label import Label


__author__ = 'Kostel Serhii'

# TODO: before create apk comment out 'lib-dynload/_csv.so' 
# in ./.buildozer/android/platform/python-for-android/src/blacklist.txt

class HelloHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return Application([
        url(r"/", HelloHandler),
        ])

class TornadoTwistedServerApp(App):
    
    def build(self):
        app = make_app()
        app.listen(8888)
        self.label = Label(text="server started\n")
        return self.label


if __name__ == '__main__':
    TornadoTwistedServerApp().run()
