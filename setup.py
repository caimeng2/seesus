from setuptools import setup

setup(
    name="seesus",
    version="0.1.0",
    description="a social, environmental, and economic sustainability classifier",
    license="GPL-3.0",
    author="Meng Cai",
    author_email="mengcai24601@gmail.com",
    packages=["seesus"],
    install_requires=["pytest","regex", "csv"],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
    url="https://github.com/caimeng2/seesus"
)
