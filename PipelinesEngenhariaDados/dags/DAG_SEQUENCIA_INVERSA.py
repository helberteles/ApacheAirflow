from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

with DAG('DAG_SEQUENCIA_INVERSA',
        description="DAG SEQUENCIA INVERSA",
        schedule_interval=None,
        start_date=datetime(2024, 7, 1),
        catchup=False) as dag:
    
    task_1 = BashOperator(task_id="task_1",bash_command="sleep 6")
    task_2 = BashOperator(task_id="task_2",bash_command="sleep 4")
    task_3 = BashOperator(task_id="task_3",bash_command="sleep 2")

    task_1.set_upstream(task_2)
    task_2.set_upstream(task_3)
