from setuptools import setup, find_packages

runtime = {
    "insights-core",
    "sqlalchemy",
}

develop = {
    "flake8==3.3.0",
    "pytest==3.0.6",
    "ipython",
}

if __name__ == "__main__":
    setup(
        name="insights_facts",
        version="0.0.1",
        description="Facts from Insights core",
        author_email="csams@redhat.com",
        license="Apache 2",
        packages=find_packages(),
        install_requires=list(runtime),
        extras_require={
            "develop": list(runtime | develop),
        },
        include_package_data=True,
        dependency_links=[
            "git+https://github.com/RedHatInsights/insights-core.git@load_finished_callback#egg=insights-core-0"
        ]
    )
