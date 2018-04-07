# Insights Facts

Install with `pip install -e .[develop] --process-dependency-links`

Run with python -m insights_facts.

A sqlite3 database called `data.db` will appear in the current directory with
a few tables.

The driver is insights_fact/__main__.py
The "framework" and sqlalchemy base stuff is in insights_facts/__init__.py
The plugins are in insights_facts/plugins
