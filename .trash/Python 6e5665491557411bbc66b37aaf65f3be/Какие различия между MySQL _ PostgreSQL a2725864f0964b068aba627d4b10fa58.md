# Какие различия между MySQL & PostgreSQL?

Answer: PostgreSQL быстрая open-source СУБД, а MySQL более прост в настройке.

MySQL: 
- чисто реляционная
- single-processing
- data types: numeric, date/time, char, spatial, json
- indexes supported: primarily b-tree, r-tree, hash and indexes for certain data types 

PostgreSQL: 
- объектно-реляционная (table inheritance, function overloading, better handling of concurrency)
- multiprocessing
- data types: += boolean, enumerated, geometric, network address, xml, hstore, arrays, ranges, composite
- B-tree, hash, GiST, SP-GiST, GIN, and BRIN

Улучшенная конкурентность в Postgres засчет MVCC, который поддерживает параллельный доступ
Type: Databases