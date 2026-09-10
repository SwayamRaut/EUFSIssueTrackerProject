from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


user = "postgres"
password = "123"
host = "db"
port = 5432
database = "issue_tracker"

#A Python object that manages connections to database server
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

#Creating a session
Session = sessionmaker(engine)


#Base is a subclass of the DeclarativeBase class
class Base(DeclarativeBase):
    """
    Pass is Python's "do nothing" statement. You need something in a class body or Python complains about an empty block. 
    pass is the convention for "this class doesn't add anything new, but I'm declaring it anyway."
    """
    pass

#This is a yield-based dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()