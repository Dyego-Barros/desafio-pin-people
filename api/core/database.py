from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker,declarative_base
import os



Base = declarative_base()


class Database:
    def __init__(self):
        self.__engine  = create_engine(os.environ.get('URL_DB'))
        self.__session = sessionmaker(autoflush=False, bind=self.__engine)
    
    
    def get_connection(self):
        
        try:
            db = self.__session()
            yield db
            
        except Exception as error:
            
            raise error
        finally:
            db.close()
            
            
    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)
