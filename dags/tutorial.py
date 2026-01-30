from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="tutorial",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["demo"],
) as dag:

    print_date = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    sleep = BashOperator(
        task_id="sleep",
        bash_command="sleep 5",
    )

    templated = BashOperator(
        task_id="templated",
        bash_command='echo "Execution date is {{ ds }}"',
    )

    print_date >> [sleep, templated]