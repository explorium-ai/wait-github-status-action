# Trigger Airflow (GCP) Dag Docker Action

This action triggers an Airflow (Composer GCP) DAG
## Inputs

```yaml
  payload:
    description: 'JSON Payload'
    required: false
    default: '{"config": {"run_type":"PR"}}'
  dag_run_id:
    description: 'custom dag run id'
    required: true
    default: ''
  client_id:
    description: 'gcp client id'
    required: true
    default: ''
  webserver_id:
    description: 'webserver id'
    required: true
    default: ''         
  dag_name:
    description: 'dag name'
    required: true
    default: ''
  google_application_credentials: 
    description: 'location of gcp credentials'
    required: true
    default: './gcp_creds.json'     
```

## Outputs

## `result`

The result of the DAG

## Example usage

```yaml
uses: explorium-ai/trigger-dag-action@v1
with:
  dag_run_id: something
  client_id: something
  webserver_id: something
  dag_name: something
  google_application_credentials: something
  payload: '{"config":"something"}'
```
