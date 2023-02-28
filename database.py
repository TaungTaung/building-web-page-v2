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