from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(2018, 4, 1),
'email': ['airflow@airflow.com'],
'email_on_failure': False,
'email_on_retry': False,
'retries': 1,
'retry_delay': timedelta(minutes=100),
# 'queue': 'bash_queue',
# 'pool': 'backfill',
# 'priority_weight': 10,
# 'end_date': datetime(2016, 1, 1),
}

directorio ='/Users/laiunce/Desktop/Entrena_red/'

dag = DAG('entrena_red', default_args=default_args)

#start of your tasks

lee_dataframe = BashOperator(task_id='lee_dataframe',
                          bash_command='python '+directorio+'lee_dataframe.py '+directorio,
                          dag=dag)


soufle = BashOperator(task_id='soufle',
                          bash_command='python '+directorio+'soufle.py '+directorio,
                          dag=dag)


separa_xt = BashOperator(task_id='separa_xt',
                          bash_command='python '+directorio+'separa_xt.py '+directorio,
                          dag=dag)

escala_x = BashOperator(task_id='escala_x',
                          bash_command='python '+directorio+'escala_x.py '+directorio,
                          dag=dag)

dummy_t = DummyOperator(
    task_id='dummy_t',
    dag=dag)

train_test_split = BashOperator(task_id='train_test_split',
                          bash_command='python '+directorio+'train_test_split.py '+directorio,
                          dag=dag)

X_Train = DummyOperator(
    task_id='X_Train',
    dag=dag)

T_Train = DummyOperator(
    task_id='T_Train',
    dag=dag)

X_Test = DummyOperator(
    task_id='X_Test',
    dag=dag)

T_Test = DummyOperator(
    task_id='T_Test',
    dag=dag)

entrena_red = BashOperator(task_id='entrena_red',
                          bash_command='python '+directorio+'entrena_red.py '+directorio,
                          dag=dag)

evalua = BashOperator(task_id='evalua',
                          bash_command='python '+directorio+'evalua.py '+directorio,
                          dag=dag)


matriz_confusion = BashOperator(task_id='matriz_confusion',
                          bash_command='python '+directorio+'matriz_confusion.py '+directorio,
                          dag=dag)



#then set the dependencies

lee_dataframe.set_downstream(soufle)
soufle.set_downstream(separa_xt)
separa_xt.set_downstream(escala_x)
separa_xt.set_downstream(dummy_t)

train_test_split.set_upstream(escala_x)
train_test_split.set_upstream(dummy_t)

train_test_split.set_downstream(X_Train)
train_test_split.set_downstream(T_Train)
train_test_split.set_downstream(X_Test)
train_test_split.set_downstream(T_Test)


entrena_red.set_upstream(X_Train)
entrena_red.set_upstream(T_Train)


evalua.set_upstream(entrena_red)
evalua.set_upstream(X_Test)
evalua.set_upstream(T_Test)

evalua.set_downstream(matriz_confusion)








