from insights_facts import Base, fact_set
from insights.parsers.redhat_release import RedhatRelease
from sqlalchemy import Boolean, Column, Integer, String


class RedhatReleaseModel(Base):
    __tablename__ = "redhat_release"

    product = Column(String)
    major = Column(Integer)
    minor = Column(Integer)
    version = Column(String)
    is_rhel = Column(Boolean)


@fact_set(RedhatRelease)
def persist(release):
    data = {
                "product": release.product,
                "major": release.major,
                "minor": release.minor,
                "version": release.version,
                "is_rhel": release.is_rhel,
           }
    return RedhatReleaseModel(**data)
