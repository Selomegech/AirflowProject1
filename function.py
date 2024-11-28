from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "my-bigquery-airflow-project"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "loadtobigquerytest",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://exchange_rates_metadata/udf.js",
        "JSONPath": "gs://exchange_rates_metadata/bg.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "my-bigquery-airflow-project:exchange_rates_dataset.history_rates",
        "inputFilePattern": "gs://exchange_rates_bucket-1/historical_currency.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://exchange_rates_metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)