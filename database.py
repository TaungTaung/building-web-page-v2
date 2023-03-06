from sqlalchemy import create_engine , text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,connect_args={
  "ssl": {
    "ssl_ca": "/home/gord/client-ssl/ca.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for dict_row in result.mappings():
      jobs.append(dict(dict_row))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),{"val":id})
    jobs = []
    for dict_row in result.mappings():
      jobs.append(dict_row)
      
    if len(jobs) == 0:
      return None
    else:
      return dict(jobs[0])

def add_application_to_db(job_id,data):
  with engine.connect() as conn:
    conn.execute(text("insert into applications (job_id, full_name, email, linkedin_url, work_experience, resume_url) values (:job_id, :full_name, :email, :linkedin_url, :work_experience, :resume_url)"),
                 {
                   "job_id": job_id,
                   "full_name":data['full_name'],
                   "email":data['email'],
                   "linkedin_url":data['linkedin_url'],
                   "work_experience":data['work_experience'],
                   "resume_url":data['resume_url']
                 })