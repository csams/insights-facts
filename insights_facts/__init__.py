"""
This module contains the SQL Alchemy base class for models and the insights core
component type for fact_sets.

A fact_set is just a thing that depends on a parser or combiner and returns an
instance (or list of instances) of a model.
"""

from insights import dr
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta


class ModelBase(DeclarativeMeta):
    """
    Provide some default columns to all the models.

    Also provide a little sugar so fields can be declared concisely in some
    cases.
    """
    def __new__(cls, name, bases, dct):
        if name not in ("ModelBase", "Base"):
            dct["id"] = Column(Integer, primary_key=True)
            dct["system_id"] = Column(String)
            dct["account"] = Column(String)

            fields = dct.get("_fields") or {}
            for k, v in fields.items():
                dct[k] = v
            if fields:
                del dct["_fields"]
        return super(ModelBase, cls).__new__(cls, name, bases, dct)


Base = declarative_base(metaclass=ModelBase)
""" Models inherit from this. """


class FactTypes(dr.TypeSet):
    fact_set = dr.new_component_type()


fact_set = FactTypes.fact_set
""" This is the decorator our model generating components will use. """
