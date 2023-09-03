from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# user='eharvnrv'
# password = '6csaMn7Egcr0DUHZ1P4rESoYQbTou6GR'
# host = 'snuffleupagus.db.elephantsql.com'
# db_name = 'eharvnrv'
# SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={
     "check_same_thread": False #add this line for sqlite only, not needed for other dbs
        }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
