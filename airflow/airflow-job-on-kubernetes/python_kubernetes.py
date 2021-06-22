
from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.providers.cncf.kubernetes.backcompat.volume_mount import VolumeMount
from airflow.providers.cncf.kubernetes.backcompat.volume import Volume
from airflow.utils.dates import days_ago

from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import os
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'python_kubernetes_workflow',
    default_args=default_args,
    description='python_kubernetes_workflow',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['python_kubernetes_workflow'],
) as dag:


    t1 = KubernetesPodOperator(
        namespace='default',
        image='python:3.7',
        image_pull_policy = 'Never',
        cmds=["python","-c", "print('hello task 1 ..................')"],
        labels={"foo": "bar"},
        name="task-1",
        is_delete_operator_pod=True,
        in_cluster=False,
        task_id="task-1",
        config_file=os.path.expanduser('~')+"/.kube/config",
        get_logs=True
    )

    t2 = KubernetesPodOperator(
        namespace='default',
        image='python:3.7',
        image_pull_policy='Never',
        cmds=["python", "-c", "print('hello task 2 ..................')"],
        labels={"foo": "bar"},
        name="task-2",
        is_delete_operator_pod=True,
        in_cluster=False,
        task_id="task-2",
        config_file=os.path.expanduser('~')+"/.kube/config",
        get_logs=True
    )


    t1 >> t2



