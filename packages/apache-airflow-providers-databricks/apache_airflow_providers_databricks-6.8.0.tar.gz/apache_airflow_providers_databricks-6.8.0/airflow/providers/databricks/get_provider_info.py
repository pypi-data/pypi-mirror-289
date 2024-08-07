# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE
# OVERWRITTEN WHEN PREPARING PACKAGES.
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-databricks",
        "name": "Databricks",
        "description": "`Databricks <https://databricks.com/>`__\n",
        "state": "ready",
        "source-date-epoch": 1722663644,
        "versions": [
            "6.8.0",
            "6.7.0",
            "6.6.0",
            "6.5.0",
            "6.4.0",
            "6.3.0",
            "6.2.0",
            "6.1.0",
            "6.0.0",
            "5.0.1",
            "5.0.0",
            "4.7.0",
            "4.6.0",
            "4.5.0",
            "4.4.0",
            "4.3.3",
            "4.3.2",
            "4.3.1",
            "4.3.0",
            "4.2.0",
            "4.1.0",
            "4.0.1",
            "4.0.0",
            "3.4.0",
            "3.3.0",
            "3.2.0",
            "3.1.0",
            "3.0.0",
            "2.7.0",
            "2.6.0",
            "2.5.0",
            "2.4.0",
            "2.3.0",
            "2.2.0",
            "2.1.0",
            "2.0.2",
            "2.0.1",
            "2.0.0",
            "1.0.1",
            "1.0.0",
        ],
        "dependencies": [
            "apache-airflow>=2.7.0",
            "apache-airflow-providers-common-sql>=1.10.0",
            "requests>=2.27.0,<3",
            "databricks-sql-connector>=2.0.0, <3.0.0, !=2.9.0",
            "aiohttp>=3.9.2, <4",
            "mergedeep>=1.3.4",
            'pandas>=2.1.2,<2.2;python_version>="3.9"',
            'pandas>=1.5.3,<2.2;python_version<"3.9"',
            "pyarrow>=14.0.1",
        ],
        "additional-extras": [
            {
                "name": "sdk",
                "description": "Install Databricks SDK",
                "dependencies": ["databricks-sdk==0.10.0"],
            },
            {
                "name": "azure-identity",
                "description": "Install Azure Identity client library",
                "dependencies": ["azure-identity>=1.3.1"],
            },
        ],
        "devel-dependencies": ["deltalake>=0.12.0"],
        "integrations": [
            {
                "integration-name": "Databricks",
                "external-doc-url": "https://databricks.com/",
                "how-to-guide": [
                    "/docs/apache-airflow-providers-databricks/operators/jobs_create.rst",
                    "/docs/apache-airflow-providers-databricks/operators/notebook.rst",
                    "/docs/apache-airflow-providers-databricks/operators/submit_run.rst",
                    "/docs/apache-airflow-providers-databricks/operators/run_now.rst",
                    "/docs/apache-airflow-providers-databricks/operators/task.rst",
                ],
                "logo": "/integration-logos/databricks/Databricks.png",
                "tags": ["service"],
            },
            {
                "integration-name": "Databricks SQL",
                "external-doc-url": "https://databricks.com/product/databricks-sql",
                "how-to-guide": [
                    "/docs/apache-airflow-providers-databricks/operators/sql.rst",
                    "/docs/apache-airflow-providers-databricks/operators/copy_into.rst",
                ],
                "logo": "/integration-logos/databricks/Databricks.png",
                "tags": ["service"],
            },
            {
                "integration-name": "Databricks Repos",
                "external-doc-url": "https://docs.databricks.com/repos/index.html",
                "how-to-guide": [
                    "/docs/apache-airflow-providers-databricks/operators/repos_create.rst",
                    "/docs/apache-airflow-providers-databricks/operators/repos_update.rst",
                    "/docs/apache-airflow-providers-databricks/operators/repos_delete.rst",
                ],
                "logo": "/integration-logos/databricks/Databricks.png",
                "tags": ["service"],
            },
            {
                "integration-name": "Databricks Workflow",
                "external-doc-url": "https://docs.databricks.com/en/workflows/index.html",
                "how-to-guide": ["/docs/apache-airflow-providers-databricks/operators/workflow.rst"],
                "logo": "/integration-logos/databricks/Databricks.png",
                "tags": ["service"],
            },
        ],
        "operators": [
            {
                "integration-name": "Databricks",
                "python-modules": ["airflow.providers.databricks.operators.databricks"],
            },
            {
                "integration-name": "Databricks SQL",
                "python-modules": ["airflow.providers.databricks.operators.databricks_sql"],
            },
            {
                "integration-name": "Databricks Repos",
                "python-modules": ["airflow.providers.databricks.operators.databricks_repos"],
            },
            {
                "integration-name": "Databricks Workflow",
                "python-modules": ["airflow.providers.databricks.operators.databricks_workflow"],
            },
        ],
        "hooks": [
            {
                "integration-name": "Databricks",
                "python-modules": [
                    "airflow.providers.databricks.hooks.databricks",
                    "airflow.providers.databricks.hooks.databricks_base",
                ],
            },
            {
                "integration-name": "Databricks SQL",
                "python-modules": ["airflow.providers.databricks.hooks.databricks_sql"],
            },
        ],
        "triggers": [
            {
                "integration-name": "Databricks",
                "python-modules": ["airflow.providers.databricks.triggers.databricks"],
            }
        ],
        "sensors": [
            {
                "integration-name": "Databricks",
                "python-modules": [
                    "airflow.providers.databricks.sensors.databricks_sql",
                    "airflow.providers.databricks.sensors.databricks_partition",
                ],
            }
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.databricks.hooks.databricks.DatabricksHook",
                "connection-type": "databricks",
            }
        ],
        "plugins": [
            {
                "name": "databricks_workflow",
                "plugin-class": "airflow.providers.databricks.plugins.databricks_workflow.DatabricksWorkflowPlugin",
            }
        ],
        "extra-links": ["airflow.providers.databricks.operators.databricks.DatabricksJobRunLink"],
    }
