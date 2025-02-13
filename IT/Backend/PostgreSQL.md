# PostgreSQL

### Типы данных

Все типы тут – [PostgreSQL : Документация: 16: Глава 8. Типы данных : Компания Postgres Professional](https://postgrespro.ru/docs/postgresql/16/datatype)

1. **Числовые типы**:
    - Целочисленные: `SMALLINT`, `INTEGER`, `BIGINT`
    - Числа с произвольной точностью: `NUMERIC`
    - С плавающей точкой: `REAL`, `DOUBLE PRECISION`
2. **Символьные типы**:
    - Фиксированная длина: `CHAR(n)` или `CHARACTER(n)`
    - Переменная длина: `VARCHAR(n)` или `CHARACTER VARYING(n)`
    - Без ограничения длины: `TEXT`
3. **Типы даты/времени**:
    - `DATE`, `TIME`, `TIMESTAMP`, `TIMESTAMPTZ`, `INTERVAL`
    - Включает поддержку часовых поясов и интервалов
4. **Логический тип** (`BOOLEAN`)
5. **Типы перечислений** (`ENUM`)
6. **UUID**
7. **XML**
8. **JSON**
9. **Массивы**
10. **Составные типы** (custom types)

### Понятия

#### Atributes (атрибуты)

Атрибуты – это по факту колонка, к которой можно обращаться как `table.column_name`. У неё есть:

- имя
- тип данных
- constraint (not null, unique, check, foreign key)
- default value

#### Tuples (кортежы)

Кортеж относится к базовой структуре данных, используемой для представления одной записи (или строки) в таблице. Кортеж содержит не только значения данных, но и дополнительную *метаинформацию*, такую как системные атрибуты e.g.

- идентификатор транзакции, который создал или удалил кортеж
- указатели на физическое местоположение кортежа в файле данных
- т.д.

### Constraints

С помощью ключевого слова CONSTRAINT можно задать имя для ограничений. 

- PK
- FK
- Unique
- Check
- Not Null
- Exclude

Имена ограничений можно задать на уровне столбцов. Они указываются после CONSTRAINT перед атрибутами.

### MVCC

MVCC (Multi-Version Concurrency Control) – это механизм управления параллельным доступом к данным в базе данных, который широко используется в PostgreSQL и других СУБД для поддержки одновременных транзакций. 

>Фишка в том, что в базе данных допускается существование нескольких «версий» одного и того же элемента данных

#### Преимущества

- Изоляция транзакций. В каждой транзакции свой “взгляд” на БД, что защищает на просмотр чужой незакомиченной даты.
- Concurrency. Несколько транзакций одновременно можно запускать.

#### Как работает

1. Получение transaction ID (TXID).
2. Чтение данных, которые закоммичены и изменений, которые собираемся сделать.
3. При операциях изменения (INSERT, UPDATE, or DELETE), создается новая версия с измененными строками и новая версия вешается на TXID – создается новый кортеж.
4. Другие транзакции увидят только “старые данные”.
5. Когда транзакция закоммичена, то проверяем, что нет конфликтов.

>Недостаток метода в том, что получаем storage overhead – много версий БД много весят.

### Транзакции в PG

Транзакции в PG следуют ACID. Ключевые понятия:

- `BEGIN`: Запускает новую транзакцию.
- `COMMIT`: Завершает текущую транзакцию и закрепляет все изменения, сделанные во время транзакции, постоянными.
- `ROLLBACK`: Отменяет все изменения, сделанные во время текущей транзакции, и завершает транзакцию.
- `SAVEPOINT`: Создает точку сохранения, к которой вы можете позже вернуться.
- `ROLLBACK TO savepoint`: Откатывает транзакцию к указанной точке сохранения.
- `RELEASE savepoint`: Удаляет точку сохранения, что позволяет зафиксировать изменения, сделанные с момента создания точки сохранения.

```sql
BEGIN; -- Start a transaction

INSERT INTO employees (name, salary) VALUES ('Alice', 5000);
INSERT INTO employees (name, salary) VALUES ('Bob', 6000);

-- Other SQL statements...

COMMIT; -- Commit the transaction and make changes permanent

-- In case of an issue, you can use ROLLBACK to revert changes
ROLLBACK; -- Roll back the transaction and undo all changes
```

#### Lock models
 
 PostgreSQL предоставляет lock modes, такие как `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, and `FOR KEY SHARE`.
 
```sql
BEGIN;
SELECT * FROM my_table WHERE id = 1 FOR UPDATE;
-- Perform updates or deletions here
COMMIT;
```

Если одна транзакция заблокировала строки с помощью этой команды, тогда параллельные транзакции не смогут заблокировать эти же строки до тех пор, пока первая транзакция не завершится, и тем самым блокировка не будет снята.

КОГДА ТАКОЕ НУЖНО ИСПОЛЬЗОВАТЬ?

9.6 МОРГУНОВ

### Обработка запроса

1. Parsing. SQL код разбивается на мелкие компоненты и создается parse tree, структура данных, которая отображет элементы запроса
2. Rewriting. Это может включать удаление ненужных условий, упрощения выражений, применения проверок безопасности.
3. Optimisation. Построения лучшего плана запроса с помощью анализа доступностью индексов, размера таблиц, сложность условий запроса. Делается расчет стоимости *каждого* плана.
4. Возврат результата.

### Утилиты

- `systemd` – система инициализации и менеджер системных процессов, используемый во многих современных дистрибутивах Linux. Он отвечает за запуск и управление фоновыми службами (демонами), включая PostgreSQL.
- `pg_ctl` – низкоуровневая утилита, предназначенная для запуска, остановки, перезапуска и управления экземплярами сервера PostgreSQL.
- pg_ctlcluster – утилита, которая предоставляет высокоуровневый интерфейс для управления кластерами PostgreSQL. Удобно для пользователей, у которых несколько кластеров PG на одной системе.
- `psql` – утилита для управления PG сервером, с которой можно делать любые операции с БД

### Сравнение PgSQL с другими СУБД

#### MySQL vs PostgreSQL

PostgreSQL быстрая open-source СУБД, а MySQL более прост в настройке.

Улучшенная конкурентность в Postgres засчет MVCC, который поддерживает параллельный доступ.

|                      | PostgreSQL                                                                                                                                                                         | MySQL                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Architecture         | Object relational; multiprocess                                                                                                                                                    | Relational; single process                                                                           |
| Data types supported | Numeric, date/time, character, boolean, enumerated, geometric, network address, JSON, XML, HSTORE, arrays, ranges, composite https://www.postgresql.org/docs/current/datatype.html | Numeric, date/time, character, spatial, JSON https://dev.mysql.com/doc/refman/8.0/en/data-types.html |
| Indexes supported    | B-tree, hash, GiST, SP-GiST, GIN, and BRIN                                                                                                                                         | Primarily B-tree; R-tree, hash, and inverted indexes for certain data types                          |
| Performance          | Suited for applications with high volume of both reads and writes                                                                                                                  | Suitable for applications with high volume of reads                                                  |
| Security             | Access control, multiple encrypted connection options https://www.postgresql.org/docs/13/runtime.html                                                                              | Access control, encrypted connections https://dev.mysql.com/doc/refman/8.0/en/security.html          |

#### Cassandra vs PostgreSQL

### Домены

Домены в PostgreSQL представляют собой способ определения пользовательских типов данных, основанных на уже существующих типах данных. Они позволяют накладывать дополнительные ограничения на столбцы в таблицах.

```sql
CREATE DOMAIN posint AS integer CHECK (VALUE > 0);
CREATE TABLE mytable (id posint);
INSERT INTO mytable VALUES(1);   -- работает
INSERT INTO mytable VALUES(-1);  -- ошибка
```

### WAL

WAL (Write-Ahead Logging) в PostgreSQL – это стандартный метод обеспечения целостности данных, который играет ключевую роль в обеспечении целостности данных и поддержке восстановления после сбоев.

Изменения в файлах с данными (где находятся таблицы и индексы) должны записываться только после того, как эти изменения были занесены в журнал, т. е. после того как записи журнала, описывающие данные изменения, будут сохранены на постоянное устройство хранения. Если следовать этой процедуре, то записывать страницы данных на диск после подтверждения каждой транзакции нет необходимости, потому что мы знаем, что если случится сбой, то у нас будет возможность восстановить базу данных с помощью журнала: любые изменения, которые не были применены к страницам с данными, могут быть воссозданы из записей журнала. (Это называется восстановлением с воспроизведением, или REDO.)

>Результатом использования WAL является значительное уменьшение количества запросов записи на диск, потому что для гарантии, что транзакция подтверждена, в записи на диск нуждается только файл журнала, а не каждый файл данных изменённый в результате транзакции.

### MATERIALIZED VIEW и VIEW 

**VIEW** – это как ярлык или ссылка на один или несколько запросов в вашей базе данных. Когда вы запрашиваете данные через представление, база данных каждый раз выполняет запросы, чтобы получить актуальную информацию. Представление не занимает дополнительного места, так как в нем не хранятся реальные данные, оно просто "показывает" данные, которые уже есть в базе.

**MATERIALIZED VIEW** – это похоже на создание снимка определенных данных и сохранение его на диске. Это значит, что данные уже вычислены и доступны для быстрого чтения, но они не обновляются автоматически вместе с изменениями в основных таблицах. Вам нужно будет время от времени обновлять (или "обновлять") этот снимок, чтобы он отражал последние изменения в данных.

```sql
CREATE VIEW customer_view AS
....
CREATE MATERIALIZED VIEW customer_summary AS
```

#### Сравнение

|                            | VIEW                                                                                           | MATERIALIZED VIEW                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Хранение                   | Виртуальная таблица, не хранится на диске.                                                     | Физическая копия базовой таблицы, хранится на диске.                     |
| Обновление                 | Автоматически обновляется при изменении данных в базовых таблицах.                             | Требует ручного обновления или обновления с помощью триггеров.           |
| Производительность         | Медленнее, так как данные вычисляются при каждом запросе.                                      | Быстрее, так как данные предварительно вычислены и сохранены.            |
| Предварительное вычисление | Отсутствует, вычисляется при каждом доступе.                                                   | Присутствует, данные сохраняются на диске.                               |
| Преимущества               | Не требует дополнительного места на диске. Может ограничить доступ к данным, упрощает запросы. | Быстрее обрабатывает запросы благодаря предварительному хранению данных. |
| Изменяемость               | Не все представления поддерживают обновление.                                                  | Необходимо обновлять вручную или с помощью триггеров.                    |

#### В каких случаях они полезны

**Представления (VIEW) полезны для:**

- **Упрощения сложных запросов**: Если вы часто выполняете сложные запросы, то можете сохранить их как представление, чтобы упростить повторное использование.
- **Ограничения доступа**: Можете показывать пользователям только определенные данные, не предоставляя доступ ко всей таблице.

**Материализованные представления (MATERIALIZED VIEW) полезны для:**

- **Ускорения чтения данных**: Поскольку данные уже вычислены и сохранены, запросы к материализованному представлению выполняются гораздо быстрее, особенно если исходные данные требуют длительных операций агрегации или соединения.
- **Снижения нагрузки на базу данных**: При работе с большими объемами данных и сложными запросами, которые не нуждаются в реальном времени, материализованные представления могут снизить частоту и сложность вычислений, выполняемых базой данных.

### `LATERAL`

`LATERAL JOIN` в PostgreSQL очень полезен в тех случаях, когда нужно получить данные из одной таблицы или подзапроса, и эти данные зависят от значений в другой таблице или подзапросе. Он позволяет использовать значения из предыдущих элементов обработки запроса в последующих элементах.

### Конфигурирование PostgreSQL

Задается двумя файлами.

- **postgresql.conf:** Общее поведение. Параметры:
	- **`listen_addresses`:** Если сервер расположен не на той же машине, что и сам PG, то требуется разрешить подключение с друго сервера. По умолчанию стоит `'*'`
	- **`port`:** This setting determines the TCP port number the server listens on.
	- **`max_connections`:** Максимальное кол-во конкурентных соединений.
	- **`shared_buffers`:** Эта общая память, которая используется одновременно всеми подключениями. Чем выше объем этих буферов, тем меньше будет нагрузка на диск.
	- **`work_mem`:** Объем памяти, который используется каждым подключением для внутренних операций.
- **pg_hba.conf:** Управление аутентификацией.

    ```
    TYPE  DATABASE  USER  ADDRESS  METHOD
    ```

#### Дополнительные настройки

##### Логирование

- **`log_destination`**: Этот параметр определяет, куда будут записываться журналы, это может быть комбинация stderr, csvlog или syslog.
- **`logging_collector`**: Включает или отключает сбор и перенаправление файлов журнала в отдельный каталог журнала.
- **`log_directory`**: Указывает каталог назначения для файлов журнала (если включен `logging_collector`).
- **`log_filename`**: Устанавливает соглашение об именовании и шаблон для файлов журнала (полезно для ротации журнала).
- **`log_statement`**: Определяет уровень SQL-операторов, которые будут записываться в журнал, например none, ddl, mod (модификация данных) или all.

##### Performance Tuning

- **`effective_cache_size`**: Указывает общий объем памяти, доступный для кэширования. Этот параметр помогает планировщику запросов оптимизировать выполнение запросов.
- **`maintenance_work_mem`**: Указывает объем памяти, доступный для операций обслуживания, таких как VACUUM и CREATE INDEX.
- **`wal_buffers`**: Определяет объем памяти, выделенной для журнала с опережающей записью (WAL).
- **`checkpoint_completion_target`** (цель завершения контрольной точки): Управляет целью завершения для контрольных точек, что помогает управлять продолжительностью и частотой сброса данных на диск.

### PL/pgSQL

PL/pgSQL (англ. Procedural Language/Postgres Structured Query Language) — процедурное расширение языка SQL, используемое в СУБД PostgreSQL.

[Postgres WAL Files and Sequence Numbers](https://www.crunchydata.com/blog/postgres-wal-files-and-sequuence-numbers)

#### Фишки

- Использование собственных типов данных (PG + Кастомные)
- Управление циклом
- Обработка исключений
- Разграничение прав

Пример:

```PL/pgSQL
CREATE FUNCTION get_total(customers_id INT) RETURNS INT AS $$
DECLARE
    total INT;
BEGIN
    SELECT SUM(order_amount) INTO total FROM orders WHERE customer_id = customers_id;
    RETURN total;
END;
$$ LANGUAGE plpgsql;
```

#### Недостатки

- Перенос приложений на другие СУБД может потребовать значительной переработки или полной перезаписи хранимых процедур и функций
- Каждая конструкция языка выполняется сервером _отдельно_. То есть, если написать какую-то функцию тяжелую, то она будет тормозить все и масштабировать это будет очень тяжело.


### Возвращаются ли ресурсы после VACUUM?

После обычного VACUUM они остаются за таблицей, а после FULL возвращаются операционной системе, потому что по факту перезаписывается вся таблица.



##      ```

## Заключение

Блокировки в PostgreSQL обеспечивают целостность данных и синхронизацию доступа к ним. Использование правильного типа блокировки помогает предотвратить проблемы конкуренции и обеспечить корректность операций в многопользовательских системах.
