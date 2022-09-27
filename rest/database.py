import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


class BaseModel():

    def __repr__(self) -> str:
        return self._repr(id=self.id)


def init_db(db_url):
    engine = sa.create_engine(db_url)
    from rest.models import Event, User
    Base.metadata.create_all(bind=engine)


def db_session():
    return sa.orm.scoped_session(sa.orm.sessionmaker(autocommit=False,
                                                     autoflush=False,
                                                     bind=sa.engine))


Base = declarative_base()
Base.query = db_session().query_property()
