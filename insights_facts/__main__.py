#!/usr/bin/env python
"""
This is a little driver that runs the components and saves their models into
some database using SQL Alchemy.
"""

from insights import dr, run
from insights.specs import Specs
from insights_facts import Base, fact_set
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# loader the stuff we care about
dr.load_components("insights.specs.default")
dr.load_components("insights.specs.insights_archive")
dr.load_components("insights.specs.sos_archive")
dr.load_components("insights_facts.plugins")

# SQL Alchemy boilerplate...
engine = create_engine("sqlite:///data.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def saver(component, broker):
    """
    This function is registered globally with insights core to watch fact_set
    components as they're evaluated.
    """
    if component in broker:
        system_id = None
        value = broker[component]

        if Specs.machine_id in broker:
            system_id = broker[Specs.machine_id].content[0]

        if isinstance(value, list):
            for v in value:
                v.system_id = system_id
            session.add_all(value)
        else:
            value.system_id = system_id
            session.add(value)

        session.commit()


# register the saver above to watch fact_sets
dr.add_observer(saver, fact_set)

# run our components
comps = dr.COMPONENTS_BY_TYPE[fact_set]
run(comps)
