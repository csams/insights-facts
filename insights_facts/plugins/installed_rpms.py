from sqlalchemy import Column, String

from itertools import chain
from insights_facts import Base, fact_set
from insights.parsers.installed_rpms import InstalledRpms


keys = "name version release arch epoch".split()


class InstalledRpmsModel(Base):
    __tablename__ = "installed_rpms"
    _fields = dict((k, Column(String)) for k in keys)


@fact_set(InstalledRpms)
def persist(rpms):
    data = []
    for pkg in chain.from_iterable(rpms.packages.values()):
        item = InstalledRpmsModel(**dict((k, getattr(pkg, k)) for k in keys))
        data.append(item)
    return data
