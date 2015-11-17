import tornado.ioloop
import tornado.web
import json
import urllib2
import logging
import weasyprint
import warnings

class WeasyPdf(tornado.web.RequestHandler):
    def post(self):
        if self.request.headers.get("Content-Type") != "text/html":
            self.set_status(400)
            self.finish()
            return

        self.add_header("Content-Type", "application/pdf")
        self.write(weasyprint.HTML(string=self.request.body).write_pdf())

    def write_error(self, status_code, **kwargs):
        self.clear()
        self.set_status(status_code)

        if status_code == 405:
            self.add_header("Allow", "POST")

        self.finish()

def main():
    warnings.filterwarnings("ignore")
    logging.getLogger("tornado.access").disabled = True

    weasypdf = tornado.web.Application([
        (r"/.*", WeasyPdf),
    ])

    weasypdf.listen(80)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
