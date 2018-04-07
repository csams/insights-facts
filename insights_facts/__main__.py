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


# SQL Alchemy boilerplate...
engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()


def loading_finished():
    Base.metadata.create_all(engine)


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
dr.add_finished_loading_callback(loading_finished)

# run our components
if __name__ == "__main__":
    dr.load_components("insights_facts.plugins")
    comps = dr.COMPONENTS_BY_TYPE[fact_set]
    run(comps, print_summary=True)
