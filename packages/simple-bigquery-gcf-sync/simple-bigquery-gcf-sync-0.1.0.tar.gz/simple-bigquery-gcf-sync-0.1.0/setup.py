from setuptools import setup, find_packages

setup(
    name="simple-bigquery-gcf-sync",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-auth",
        "google-cloud-bigquery",
        "pandas",
    ],
    author="Carbonemys",
    author_email="carbonemys@carbonemys.nl",
    description="A BigQuery connector for easy data syncing for your custom import. Checks the last date in the table and only appends new data or creates a new table. Made for Google Cloud Functions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/carbonemys/simple-bigquery-gcf-sync",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
