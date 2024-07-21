from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG('DAG_PRECEDENCIA',
        description="DAG DE PRECEDENCIA",
        schedule_interval=None,
        start_date=datetime(2024, 7, 1),
        catchup=False)


task_process_1 = BashOperator(task_id="task_process_1",bash_command="sleep 5",dag=dag)

task_process_2 = BashOperator(task_id="task_process_2",bash_command="sleep 5",dag=dag)

task_end = BashOperator(task_id="task_end",bash_command="sleep 5",dag=dag)

[task_process_1,task_process_2] >> task_end