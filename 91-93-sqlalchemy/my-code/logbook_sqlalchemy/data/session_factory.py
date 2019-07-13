import sqlalchemy
import sqlalchemy.orm


import db.db_folder as db_folder


from models.mode_base import ModelBase


from models import flight, aircraft

__factory = None


def global_init():
    global __factory
    
    full_file = db_folder.get_db_path('flylogbook.sqlite')
    conn_str = 'sqlite:///' + full_file
    
    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)
    
    __factory = sqlalchemy.orm.sessionmaker(bind=engine)
    

def create_session():
    global __factory
    
    if __factory is None:
        global_init()
        
    return __factory()