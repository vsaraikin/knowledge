# Celery

**Celery** — **это** программа, которая отслеживает **задачи** (tasks), которые необходимо выполнить, и в которой есть набор **обработчиков** (workers), которые будут выполнять эти задачи. Основной смысл в том, что она (программа) может выполнять несколько задач **параллельно** и что она **не блокирует** поставщиков (producers) этих самых задач.

## Best practices

1. Don't use the database as your AMQP Broker
2. Use more Queues (ie. not just the default one)
3. Use priority workers
4. Use Celery's error handling mechanisms
5. Use Flower - for monitoring
6. Keep track of results only if you really need them
7. Don't pass Database/ORM objects to tasks

After giving this talk at a local Python meetup a few people suggested I add this to the list. What's it all about? You shouldn't pass Database objects (for instance your User model) to a background task because the serialized object might contain stale data. What you want to do is feed the task the User id and have the task ask the database for a fresh User object.

## Celery beat

**Celery beat -** a **scheduler;** it **kick** off tasks at regular intervals, that are then executed by available worker nodes in the cluster.

## Что будет, если celery worker упал, но не доделал task

Использовать Task Retry Decorator.
## Приоритеты в celery