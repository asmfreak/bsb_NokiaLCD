import web
from NokiaLCDServer import server

urls = (
    '', server.app,
)
app = web.application(urls, locals())
if __name__ == "__main__":
    app.run()
