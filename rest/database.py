import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        '''
        Helper for __repr__
        '''
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"

def init_db():
    from rest.models import Event, User
    Base.metadata.create_all(bind=engine)
