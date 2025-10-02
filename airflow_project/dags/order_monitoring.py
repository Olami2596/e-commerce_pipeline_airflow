from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
# import snowflake.connector
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'email': ['tijaniabdulhakeemola@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='order_monitoring_dag',
    default_args=default_args,
    schedule='@hourly',
    start_date=datetime.now() - timedelta(days=1),
    catchup=False
) as dag:
  dbt_run = BashOperator(
      task_id='run_dbt_models',
      bash_command='cd /opt/airflow/dbt_ecommerce && dbt run'
  )

  check_orders = BashOperator(
      task_id='check_delayed_orders',
      bash_command="python /opt/airflow/dags/utils/check_delayed_orders.py"
  )


  dbt_run >> check_orders