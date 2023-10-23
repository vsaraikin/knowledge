# Вопросы
1) чем асинхронность отличается от многопоточности. Приведите пример, когда лучше применить одно , а когда другое?
2) как передать информацию из одного треда в другой
3) вы асинхронно запустили функцию1 и функцию2. Как запустить функцию3 после того как функция1 завершит выполнение ? а  по срабатыванию триггера в функции 2 ?
4) вы создали 2 потока и запускаете внутри них всякое. Как передать данные из одного потока в другой ? Как по триггеру срабатывающему внутри потока - инициализировать новый ?
5) что такое консистентность , транзакционность , атомарность ?

# Ответы
1. Асинхронность – это такое свойство, когда программа выполняется в одном потоке и не дожидается завершения одной задачи, а сразу переходит к другой. Многопоточность – это выполнение задач в нескольких потоках, а потоки -- это сущности внутри одного процесса. То есть, когда программа общается с сервером и ждет ответа, то логично переходить к другой и не дожидаться ответа (то есть хорошо подходит для веба). Многопоточность хорошо подходит для I/O bound задач (чтение/запись).
2. Можно с помощью модуля `queue`. Создаем объект этого очереди и прокидываем в этот объект через метод put нужную переменную. Либо же можно использовать глобальную переменную и получать к ней доступ с разных потоков. Возможно, второй вариант – это не совсем то, что спрашивается, но потоки делят память внутри одного процесса и, если мы создадим глобальную переменную X, то доступ к ней и ее изменению получат сразу все треды и тем самым можно также делиться информацией.
3. Тут не уточнилось, но я предположу, что `func3` тоже асинхронная. Тогда мы можем создать еще одну функцию `f1`, которая будет в себе иметь `func1()` и `func3()` (своего рода инкапсуляция). Например:
   
```python
import asyncio

async def func1():
    print('1 has started')
    await asyncio.sleep(1)
    print('1 has finished')

async def func2():
    print('2 has started')
    await asyncio.sleep(1)
    print('2 has finished')
    

async def func3():
    print('3 has started')
    await asyncio.sleep(1)
    print('3 has finished')


async def f1():
    await func1()
    await func3()
    

async def main():    
    tasks = [f1(), func2()]
    await asyncio.gather(*tasks)
    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
   
Output:
```python
1 has started
2 has started
1 has finished # as soon as 1st task finished, we go the 3rd
3 has started
2 has finished
3 has finished
```

"_а  по срабатыванию триггера в функции 2?_" Например, для этого есть `asyncio.Event()`. Мы можем уведомить другие корутины о наступлении события. Например:

```python
import asyncio

async def func1():
    print('1 has started')
    print('1 has finished')
    

async def func2(event):
    print('2 has started')
    event.set() # notify others that event is True
    await asyncio.sleep(5)
    print('2 has finished')
    

async def func3():
    print('3 has started')
    print('completing 3rd task')
    print('3 has finished')
    

async def main():
    event = asyncio.Event()

    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2(event))
    
    await event.wait()
    await func3()
    await task1
    await task2

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Output:
```python
1 has started
1 has finished
2 has started
3 has started
completing 3rd task
3 has finished
2 has finished
```

4. Первый вопрос повторяет вопрос #2, потому что треды и потоки – это одно и тоже, ровно как и данные с информацией в нашем условном случае. Касаемо триггера, то это можно сделать следующим образом:
  ```python
import threading

def func1():
    print('1 started')
    e.set() # notify that event has happened
    
def func2():
    print('2 started')
        

e = threading.Event()
t1 = threading.Thread(func1())
t1.start()
t1.join()

if e.is_set():
    t2 = threading.Thread(func2())
    t2.start()
  ```

5. Это три важных свойства в БД. 
	1.  Консистентность – это свойство, которое обеспечивает, что данные в базе данных всегда находятся в верном состоянии и не противоречят друг другу.
	2.  Транзакционность – это свойство группировки нескольких операций с базой данных в единую атомарную единицу – транзакцию.
	3. Атомарность гарантирует, что каждая транзакция будет выполнена полностью или не будет выполнена совсем. Не допускаются промежуточные состояния.