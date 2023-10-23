# Frontend

[70 вопросов по JavaScript для подготовки к собеседованию](https://habr.com/ru/post/486820/)

[GitHub - YauhenKavalchuk/interview-questions: Популярные HTML / CSS / JavaScript / ECMAScript / TypeScript / React / Vue / Angular / Node вопросы на интервью и ответы на них (https://tinyurl.com/wxysrpsy)](https://github.com/YauhenKavalchuk/interview-questions)

[GitHub - likezninjaz/react-ru-interview-questions: Здесь собраны самые популярные вопросы, задаваемые на русскоязычных собеседованиях разработчика React.js, и ответы на них. Тематика вопросов включает в себя как основы JavaScript и веб-технологий так и глубокое понимание работы React.js](https://github.com/likezninjaz/react-ru-interview-questions)

# JavaScript

### `var` vs `let` vs `const`

### Global Scope vs Function Scope vs Block Scope

Global Scope: Variables declared outside any function or curly braces ’{}’ have Global Scope, and can be accessed from anywhere within the same Javascript code. **`var`**, **`let`** and **`const`** all provide this Scope.

Function Scope: Variables declared within a function can only be used within that same function. Outside that function, they are undefined. **`var`**, **`let`** and **`const`** all provide this Scope.

Block Scope: A block is any part of JavaScript code bounded by ’{}‘. Variables declared within a block can not be accessed outside that block. This Scope is only provided by the **`let`** and **`const`** keywords. If you declare a variable within a block using the **`var`** keyword, it will NOT have Block Scope.

### Data types

- Число **«number»** - Единый тип число используется как для целых, так и для дробных чисел. Существуют специальные числовые значения Infinity (бесконечность) и NaN (ошибка вычислений). Например, бесконечность Infinity получается при делении на ноль. Ошибка вычислений NaN будет результатом некорректной математической операции.
- Строка **«string»**
- Булевый (логический) тип **«boolean»**
- Специальное значение **«null»** - В JavaScript null не является «ссылкой на несуществующий объект» или «нулевым указателем», как в некоторых других языках. Это просто специальное значение, которое имеет смысл «ничего» или «значение неизвестно».
- Специальное значение **«undefined»** - Значение undefined, как и null, образует свой собственный тип, состоящий из одного этого значения. Оно имеет смысл «значение не присвоено». Если переменная объявлена, но в неё ничего не записано, то её значение как раз и есть undefined.
- Символы **«symbol»** - «Символ» представляет собой уникальный идентификатор. Создаются новые символы с помощью функции Symbol(). Символы гарантированно уникальны. Даже если мы создадим множество символов с одинаковым описанием, это всё равно будут разные символы. Описание – это просто метка, которая ни на что не влияет.
- Тип «number» не может содержать числа больше, чем (21), или меньше, чем -(21). Тип **«bigint»** даёт возможность работать с целыми числами произвольной длины.
- Объекты **«object»** - Первые 7 типов называют «примитивными». Особняком стоит восьмой тип: «объекты». Он используется для коллекций данных и для объявления более сложных сущностей. Объявляются объекты при помощи фигурных скобок {...}

### DOM

### Virtual DOM

### Static метод

### Set, Map, WeakSet и WeakMap

### Event loop

Движок браузера выполняет JavaScript в одном потоке. Для потока выделяется область памяти — стэк, где хранятся фреймы (аргументы, локальные переменные) вызываемых функций.

Список событий, подлежащих обработке формируют очередь событий. Когда стек освобождается, движок может обрабатывать событие из очереди. Координирование этого процесса и происходит в event loop.

Это по сути бесконечный цикл, в котором выполняются многочисленные обработчики событий. Если очередь пустая — движок браузера ждет, когда поступит событие. Если непустая — первое в ней событие извлекается и его обработчик начинает выполняться. И так до бесконечности.

### Замыкание

Замыкание — это комбинация функции и лексического окружения, в котором эта функция была объявлена. Это окружение состоит из произвольного количества локальных переменных, которые были в области действия функции во время создания замыкания.

Так как нету `private` & `protected` полей, то это хороший способ что-то скрыть.

### Что такое прототип объекта в JavaScript?

Прототипы - это механизм, с помощью которого объекты JavaScript наследуют свойства друг от друга.

### Ключесов слово `This`

### Промисы

### Event Loop

# React

### JSX

### Render

### Props 

## Frontend