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
                'city': job.city,
                'companyLogo': job.companyLogo,
                'companySize': job.companySize,
                'companyName': job.companyName,
                'industryField': job.industryField,
                'financeStage': job.financeStage,
                'website': job.website,

                'salary': job.salary,
                'jobNature': job.jobNature,
                'createTime': str(job.createTime),
                'positionName': job.positionName,
                'positionType': job.positionType,
                'positionAdvantage': job.positionAdvantage,
                'positionFirstType': job.positionFirstType,
                'jobDescription': job.jobDescription,
                'workTime': job.workTime,

                'minWorkYear': job.minWorkYear,
                'maxWorkYear': job.maxWorkYear,
                'education': job.education,

                'positionId': job.positionId,
                'originUrl': job.originUrl,
                'fromWhich': job.fromWhich
            }
            for job in DBSession.query(JobModel).all()
            ]
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
