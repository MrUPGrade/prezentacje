import cherrypy
from sqlalchemy.orm import joinedload

from dal_opt.db import session_factory, Cinema

session = session_factory()


class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        cinemas = session.query(Cinema).options(joinedload('films'))
        cinemas_as_dict = [c.asdict(follow=['films']) for c in cinemas]

        return cinemas_as_dict


cherrypy.quickstart(HelloWorld())
