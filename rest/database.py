from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class BaseModel():

#     def __repr__(self) -> str:
#         return self._repr(id=self.id)


# class Database():
#     def __init__(self):
#         self.Model = declarative_base()
#         pass

#     def init_app(self, app):
#         self.engine = sa.create_engine(app.config["DATABASE_URI"])

#         self.session = sa.orm.scoped_session(sa.orm.sessionmaker(autocommit=False,
#                                                                  autoflush=False,
#                                                                  bind=self.engine))

#         from rest.models import Event, User
#         self.Model.metadata.create_all(bind=self.engine)
#         self.Model.query = self.session.query_property()

#     def session(self):
#         return sa.orm.scoped_session(sa.orm.sessionmaker(autocommit=False,
#                                                          autoflush=False,
#                                                          bind=self.engine))
