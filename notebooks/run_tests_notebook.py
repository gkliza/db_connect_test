# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks-Connect Test
# MAGIC This notebook is designed to run the unit tests on the `db_connect_test` package from inside Databricks.
# MAGIC
# MAGIC This shows how to keep the `databricks-connect` library isolated from a Databricks environment so that, specifically pytest, unit tests can be run both from within an IDE and from Databricks without causing conflicts with PySpark.

# COMMAND ----------

# Uncomment and run this if you did not install pytest on the cluster
# %pip install pytest

# COMMAND ----------

import pytest
import os
import sys

# Get the path to this notebook, for example "/Workspace/Repos/{username}/{repo-name}".
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
print(notebook_path)

# COMMAND ----------

# Get the repo's root directory name (up two directories)
repo_root = os.path.dirname(os.path.dirname(notebook_path))
print(repo_root)

# COMMAND ----------

# Prepare to run pytest from the repo.
os.chdir(f"/Workspace/{repo_root}")
sys.path.append(f"/Workspace/{repo_root}")
sys.path.append(f"/Workspace/{repo_root}/src()")
print(os.getcwd())

# COMMAND ----------

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."
