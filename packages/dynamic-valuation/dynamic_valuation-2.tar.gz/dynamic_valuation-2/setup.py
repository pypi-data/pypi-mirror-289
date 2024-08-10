from setuptools import setup, find_packages

setup(
    name="dynamic_valuation",
    version="2",
    author="Eric Larson",
    author_email="ericl3@illinois.edu",
    description="Find the present value of a capital asset stocks and/or\
    flows subject to an equation of motion.",
    packages=['dynamic_valuation'],
    install_requires=["numpy","matplotlib","scipy","pandas"]
)
