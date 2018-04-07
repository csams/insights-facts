# Insights Facts

This is an experimental package that allows developers to convert insights
components into SQLAlchemy models that get stored in a supported data store.

Install with `pip install -e .[develop] --process-dependency-links`.

Run on the local machine with `python -m insights_facts` or `python -m insights -p insights_facts`.

Run on an archive with `python -m insights_facts -- <archive>` or `python -m insights -p insights_facts -- <archive>`.

A sqlite3 database called `data.db` will appear in the current directory with a few tables.

The driver and insights-core callback hooks are in `insights_facts/__main__.py`.

The "framework" and sqlalchemy stuff are in `insights_facts/__init__.py`.

Plugins for a few parsers are in `insights_facts/plugins`.
