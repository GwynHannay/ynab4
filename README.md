# YNAB4
![Top Language](https://img.shields.io/github/languages/top/GwynHannay/ynab4)
![Licence](https://img.shields.io/github/license/GwynHannay/ynab4)
![Last Commit](https://img.shields.io/github/last-commit/GwynHannay/ynab4)
![Latest Release](https://img.shields.io/github/v/release/GwynHannay/ynab4)
![Total Downloads](https://img.shields.io/github/downloads/GwynHannay/ynab4/total)

Python integrations with YNAB4

## YNAB4 to BigQuery

The first component built here is a simple import of your YNAB4 budget into BigQuery. This requires you to have your own Google Cloud Platform project, which has a free tier, and ensure that the BigQuery API is enabled.

A potential limitation in this version of the code is that the BigQuery schema is built using auto-detect. Auto-detect uses the first 100 rows of your file to build the table schema, so if there are fields not in those first 100 rows then they will be omitted.

### Usage

You need:
* A Google Cloud Platform project with the BigQuery API enabled.
* A BigQuery dataset created for your tables.
* The JSON key of a Service Account with the roles ``BigQuery Data Editor`` and ``BigQuery Job User``.
* The BigQuery API client library for Python, which you can install by running ``python -m pip install -r requirements.txt``.
* Your ``Budget.yfull`` file from YNAB. There's a sample in this repository, but you can find yours inside your YNAB folders. [This post](https://jack.codes/projects/2016/09/13/reversing-the-ynab-file-format-part-1) by [Jack Turnbull](https://github.com/jackturnbull) might be able to help you locate your file if you're not sure about it.

Set up your config file in ``config/bigquery.ini``.

![Screen Shot 2022-04-22 at 2 31 35 pm](https://user-images.githubusercontent.com/8345824/164616832-09ebea59-1d29-4754-883b-d1d2e978dcb1.png)
* _BudgetFile_: This is the path and filename to your YNAB4 budget file. Right now, if you were to simply run the ``main.py`` file in the root folder of this repository, it would run the sample budget file.
* _ServiceAccountKey_: This is the path and filename for your GCP Service Account's JSON key. This example would use a JSON file called ``ynab4_gcp_key.json`` located in a ``secrets`` folder under the root directory of this repository.
* _ProjectID_: Your Google Cloud Platform project ID, which is not always the same as the project name! Check your project ID in the main dashboard on GCP.
* _Dataset_: The name of the dataset you've created in BigQuery for these tables.
* _Location_: The region in which your BigQuery dataset was created.

## General Information

**Language:** Python 3.8.13

Distributed under the GNU GPL v3 license. See ``LICENSE`` for more information.
