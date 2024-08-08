# Fix service account handling
# Add optional patitioning time and true/false

import os
from datetime import datetime, timedelta

import google.auth
from google.api_core.exceptions import NotFound
from google.cloud import bigquery
from google.oauth2 import service_account


class BigQueryConnector:
    project_id = None
    dataset_id = None
    table_id = None
    client = None

    @classmethod
    def initialize(cls, project_id, dataset_id, table_id):
        cls.project_id = project_id
        cls.dataset_id = dataset_id
        cls.table_id = table_id

        # Auth
        env = os.getenv("ENV")
        if env == "production":
            print("⏩ Running in GCP")
            credentials, project = google.auth.default()
        else:
            print("⏩ Running locally with key.json")
            credentials = service_account.Credentials.from_service_account_file(
                "key.json"
            )
        cls.client = bigquery.Client(project=project_id, credentials=credentials)

        print(
            f"⏩ Initialized BigQueryConnector for table {cls.project_id}.{cls.dataset_id}.{cls.table_id}"
        )

    @classmethod
    def get_table_ref(cls):
        return cls.client.dataset(cls.dataset_id).table(cls.table_id)

    @classmethod
    def create_table(cls, schema):
        table_ref = cls.get_table_ref()
        table = bigquery.Table(table_ref, schema=schema)
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.MONTH,
            field="date",
        )
        cls.client.create_table(table)
        print(f"Created partitioned table {cls.table_id}")

    @classmethod
    def load_data(cls, df):
        if df.empty:
            print("⚠️ No data to load.")
            return

        table_ref = cls.get_table_ref()
        job = cls.client.load_table_from_dataframe(df, table_ref)
        job.result()
        print(f"⏩ Loaded {len(df)} rows into {cls.table_id}")

    @classmethod
    def get_most_recent_date(cls):
        query = f"""
        SELECT MAX(date) as max_date 
        FROM `{cls.project_id}.{cls.dataset_id}.{cls.table_id}`
        """
        query_job = cls.client.query(query)
        results = query_job.result()
        max_date = next(iter(results)).max_date
        print(f"⏩ Most recent date in {cls.table_id}: {max_date}")
        return max_date

    @classmethod
    def ensure_table_exists(cls, schema):
        try:
            cls.get_most_recent_date()
        except NotFound:
            print(f"⏩ Table {cls.table_id} not found. Creating new table.")
            cls.create_table(schema)

    @classmethod
    def get_date_range(cls, default_start_date):
        try:
            most_recent_date = cls.get_most_recent_date()
            start_date = (
                most_recent_date + timedelta(days=1) if most_recent_date else None
            )
        except NotFound:
            print(f"⚠️ Table {cls.table_id} not found.")
            start_date = None

        if not start_date:
            start_date = datetime.fromisoformat(default_start_date).date()

        end_date = datetime.now().date() - timedelta(days=1)

        if start_date > end_date:
            print(
                f"⏩ Start date {start_date} is after end date {end_date}. No new data to process."
            )
            return None, None

        print(f"⏩ Processing data range: {start_date} to {end_date}")
        return start_date, end_date
