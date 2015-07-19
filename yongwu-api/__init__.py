# coding:utf-8


import falcon
from sqlalchemy.engine import create_engine
import simplejson as json

from .module import DBSession, Base, JobModel


class JobResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        job_list = [
            {
                'id': job.id,
                'company': job.company
            }
            for job in DBSession.query(JobModel).all()
            ]
        resp.body = json.dumps(job_list)

    def on_post(self, req, resp):
        new_job = json.loads(req.stream.read())
        DBSession.add(JobModel(**new_job))
        resp.body = json.dumps({'status': 'ok'})


engine = create_engine(
    "mysql+pymysql://root:yongwu@mysql/yongwu?charset=utf8")
DBSession.configure(bind=engine)
Base.metadata.bind = engine
app = falcon.API()
app.add_route('/', JobResource())
