kubernetes_min_pod = KubernetesPodOperator(
    # The ID specified for the task.
    task_id='selenium',
    name='selenium',
    namespace='default',
    image='us.gcr.io/james-340405/selenium')