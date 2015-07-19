# coding:utf-8


import falcon
from sqlalchemy.engine import create_engine
import simplejson as json

from .module import DBSession, Base, JobModel


class JobResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        job_list = []
        for job in DBSession.query(JobModel).all():
            job = dict(job.__dict__)
            del job['_sa_instance_state']
            job['createTime'] = str(job['createTime'])
            job_list.append(job)
        DBSession.close()
        resp.body = json.dumps(job_list)

    def on_post(self, req, resp):
        new_job = json.loads(req.stream.read())
        try:
            DBSession.add(JobModel(**new_job))
            DBSession.commit()
        except:
            DBSession.rollback()
        finally:
            DBSession.close()

        resp.body = json.dumps({'status': 'ok'})


engine = create_engine(
    "mysql+pymysql://root:yongwu@mysql/yongwu?charset=utf8")
DBSession.configure(bind=engine)
Base.metadata.bind = engine
app = falcon.API()
app.add_route('/', JobResource())
