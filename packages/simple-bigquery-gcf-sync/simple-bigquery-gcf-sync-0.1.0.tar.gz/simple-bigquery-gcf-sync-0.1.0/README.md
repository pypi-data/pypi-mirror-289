# simple-bigquery-gcf-sync

Created so you only have to focus on the logic for your custom connector. The package takes care of:

- Creating a table if it does not exist
- Getting the latest date in the table if it exists, setting start date to the following day until yesterday
- Conditionally running locally or using a Cloud Function service account

Note:

- Currently defaults to montly table partitioning
- For running locally your project should contain service account `key.json` in the same folder
- You must provide a `default_start_date` and `source_schema`

# Example usage

```python
# Settings
source_schema = [
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("order_id", "STRING"),
    bigquery.SchemaField("order_amount", "FLOAT"),
]
default_start_date = "2022-01-01"  # Required

def get_data_from_source(start_date, end_date):
    # Your custom source logic, should use start and end date


def main(request):
    print("⏩ Cloud Function invoked")
    project_id = request.args.get("project_id")
    dataset_id = request.args.get("dataset_id")
    table_id = request.args.get("table_id")

    BigQueryConnector.initialize(project_id, dataset_id, table_id)
    BigQueryConnector.ensure_table_exists(source_schema)
    start_date, end_date = BigQueryConnector.get_date_range(default_start_date)
    data = get_data_from_source(start_date, end_date, pub_key, priv_key)
    BigQueryConnector.load_data(data)

    print("✅ Data processing completed successfully")
    return


### For local testing, do not copy into cloud function
if __name__ == "__main__":

    class MockRequest:
        args = {
            "project_id": "project-name",
            "dataset_id": "dataset-name",
            "table_id": "table-name",
        }

    main(MockRequest())
```
