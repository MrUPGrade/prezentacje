import cherrypy
import os


class HelloWorld(object):
    def __init__(self, db_host):
        self.db_host = db_host

    @cherrypy.expose
    def index(self, q=None):
        if q == 'porn':
            raise Exception('Porn is bad for you!')

        cherrypy.log('Connecting to %s' % self.db_host)

        return 'Hello World!'


cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080,
})

if __name__ == '__main__':
    try:
        DB_HOST = os.environ['DB_HOST']
    except KeyError:
        print('need setting "%s" for running application' % 'DB_HOST')
        raise

    cherrypy.quickstart(HelloWorld(DB_HOST))
