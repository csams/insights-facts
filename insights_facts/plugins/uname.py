from insights_facts import Base, fact_set
from insights.parsers.uname import Uname
from sqlalchemy import Column, String


class UnameModel(Base):
    __tablename__ = "uname"
    _fields = dict((k, Column(String)) for k in Uname.keys)


@fact_set(Uname)
def persist(uname):
    return UnameModel(**dict((k, str(uname.data[k])) for k in Uname.keys))
