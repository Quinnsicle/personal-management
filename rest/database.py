import sqlalchemy as sa

engine = sa.create_engine('sqlite:////tmp/test.db')
db_session = sa.orm.scoped_session(sa.orm.sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


Base = sa.ext.declarative.declarative_base()
Base.query = db_session.query_property()

import typing

class BaseModel():

    def __repr__(self) -> str:
        return self._repr(id=self.id)

def init_db():
    from rest.models import Event, User
    Base.metadata.create_all(bind=engine)
