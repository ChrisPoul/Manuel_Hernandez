from setuptools import find_packages, setup

setup(
    name="ComedorManager",
    verision="1.0.0",
    author="Christopher Poulsen",
    author_email="chris30-1@hotmail.com",
    description="Helps an accountant keep track of all transactions",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
    ]
)