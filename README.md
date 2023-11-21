# DB_Connect Test Project
## Description
This is a python file that aims to test how to set up pytest so it can use databricks-connect to connect to a databricks cluster and run tests on the cluster, as well as running testing from a databricks notebook.

## Installation
First you will need to fork this repository into one that can integrate with your Databricks workspace.

Then clone this repository into your local machine.

## Setup
In the local environment, you will need to install the following:
- databricks-utils
- pytest

### Databricks-connect
databricks-connect has conflicts with pyspark. When setting up a new virtual environment do not install pyspark firs. Instructions for setting up databricks-connect can be done by following the instructions here: https://docs.databricks.com/dev-tools/databricks-connect.html and here: https://docs.databricks.com/en/dev-tools/databricks-connect/python/install.html

### Environment Variables
You will need to set up the following environment variables:
- DB_HOST: the url of your databricks instance
- DB_TOKEN: [personal access token](https://docs.databricks.com/en/administration-guide/access-control/tokens.html) for your Databricks User or Service Principal
- DB_CLUSTER_ID: the id of the cluster this instance will use

### Environment Variables in PyCharm / IntelliJ
Environment Variables are cumbersome in PyCharm. Variables can be set for the Python Console, the Terminal, or for each run configuration triggere through the code view.

When executing tests from the code view, a new configuration is created for each test. Before running any tests, you should edit the default configuration for Run -> Edit Configurations -> Edit Configuration Templates -> Python tests -> [Autodetect, pytest].

## Other Notes
databricks-connect 13.* and up implement a SparkConnect that no longer supports .rdd functions.

## Running Tests
### From PyCharm / IntelliJ
Tests can be run from the code view by right clicking on the test file or test function and selecting "Run 'pytest in test_file.py'". This will create a new run configuration for the test. You can edit the run configuration to add environment variables.

### From Databricks Notebook
Add this repository as a repo to your databricks repos. You can then run the `run_test_notebook.py`.