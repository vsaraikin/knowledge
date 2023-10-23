# Python Web Frameworks

- [Frameworks](#frameworks)
  * [Django](#django)
    + [Структура проекта](#%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
    + [Архитектура Django](#%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0-django)
    + [QuerySet](#queryset)
    + [Lazy Loading Django](#lazy-loading-django)
    + [Абстрактные модели](#%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B5-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8)
    + [Что такое сигналы? Зачем они нужны? Назови основные?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%81%D0%B8%D0%B3%D0%BD%D0%B0%D0%BB%D1%8B-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D0%BE%D0%BD%D0%B8-%D0%BD%D1%83%D0%B6%D0%BD%D1%8B-%D0%BD%D0%B0%D0%B7%D0%BE%D0%B2%D0%B8-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5)
    + [Как реализуется связь M2M на уровне базы данных?](#%D0%BA%D0%B0%D0%BA-%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D1%83%D0%B5%D1%82%D1%81%D1%8F-%D1%81%D0%B2%D1%8F%D0%B7%D1%8C-m2m-%D0%BD%D0%B0-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
    + [Что такое n + 1 проблема и как ее можно избежать в Джанго?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-n--1-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B8%D0%B7%D0%B1%D0%B5%D0%B6%D0%B0%D1%82%D1%8C-%D0%B2-%D0%B4%D0%B6%D0%B0%D0%BD%D0%B3%D0%BE)
    + [Q выражение и его использование?](#q-%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8-%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
    + [F выражение](#f-%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)
    + [Что такое Middleware, для чего используется, как реализуется?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-middleware-%D0%B4%D0%BB%D1%8F-%D1%87%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D1%82%D1%81%D1%8F-%D0%BA%D0%B0%D0%BA-%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D1%83%D0%B5%D1%82%D1%81%D1%8F)
    + [Назови основные middlewares и их назначение](#%D0%BD%D0%B0%D0%B7%D0%BE%D0%B2%D0%B8-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-middlewares-%D0%B8-%D0%B8%D1%85-%D0%BD%D0%B0%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
    + [Опишите алгоритм работы CSRF middleware](#%D0%BE%D0%BF%D0%B8%D1%88%D0%B8%D1%82%D0%B5-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-csrf-middleware)
    + [Для чего используется класс Meta в Django models?](#%D0%B4%D0%BB%D1%8F-%D1%87%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D1%82%D1%81%D1%8F-%D0%BA%D0%BB%D0%B0%D1%81%D1%81-meta-%D0%B2-django-models)
    + [Что такое менеджеры в Django?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80%D1%8B-%D0%B2-django)
    + [Преимущества и недостатки Django ORM](#%D0%BF%D1%80%D0%B5%D0%B8%D0%BC%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0-%D0%B8-%D0%BD%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BA%D0%B8-django-orm)
    + [Разница select_related и prefetch_related](#%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-select_related-%D0%B8-prefetch_related)
    + [Что такое миксины](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D0%BC%D0%B8%D0%BA%D1%81%D0%B8%D0%BD%D1%8B)
    + [Как лучше отправлять форму GET или POST?](#%D0%BA%D0%B0%D0%BA-%D0%BB%D1%83%D1%87%D1%88%D0%B5-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%82%D1%8C-%D1%84%D0%BE%D1%80%D0%BC%D1%83-get-%D0%B8%D0%BB%D0%B8-post)
    + [Кэширование в Django](#%D0%BA%D1%8D%D1%88%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-django)
    + [Django Field классы](#django-field-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B)
    + [Объясните жизненный цикл ответа(Response lifecycle) Django?](#%D0%BE%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D0%B8%D1%82%D0%B5-%D0%B6%D0%B8%D0%B7%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%86%D0%B8%D0%BA%D0%BB-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0response-lifecycle-django)
    + [ASGI & WSGI](#asgi--wsgi)
    + [Что такое функция django.shortcuts.render?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F-djangoshortcutsrender)
    + [Как использовать файловые сессии?](#%D0%BA%D0%B0%D0%BA-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D1%8B%D0%B5-%D1%81%D0%B5%D1%81%D1%81%D0%B8%D0%B8)
    + [Разница между Django OneToOneField и ForeignKey Field](#%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-django-onetoonefield-%D0%B8-foreignkey-field)
    + [Как получить SQL-запрос из набора запросов?](#%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-sql-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%B8%D0%B7-%D0%BD%D0%B0%D0%B1%D0%BE%D1%80%D0%B0-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2)
    + [Как можно объединить несколько QuerySet в вьюшках?](#%D0%BA%D0%B0%D0%BA-%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%BE%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-queryset-%D0%B2-%D0%B2%D1%8C%D1%8E%D1%88%D0%BA%D0%B0%D1%85)
  * [DRF](#drf)
    + [DRF методы построения API](#drf-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%B8%D1%8F-api)
    + [Serializer в DRF](#serializer-%D0%B2-drf)
    + [Для чего используется класс Meta в Django serializer?](#%D0%B4%D0%BB%D1%8F-%D1%87%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D1%82%D1%81%D1%8F-%D0%BA%D0%BB%D0%B0%D1%81%D1%81-meta-%D0%B2-django-serializer)
    + [Система аутентификации в Django](#%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-django)
    + [DRF permissions](#drf-permissions)
  * [Flask](#flask)
    + [Django vs Flask](#django-vs-flask)
    + [Что быстрее Flask или Django и почему?](#%D1%87%D1%82%D0%BE-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%B5%D0%B5-flask-%D0%B8%D0%BB%D0%B8-django-%D0%B8-%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83)
  * [FastAPI](#fastapi)
    + [Почему FastAPI?](#%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83--fastapi)
    + [миграции alembic](#%D0%BC%D0%B8%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-alembic)
    + [related модели sqlalchemy](#related-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8-sqlalchemy)
  * [JWT](#jwt)
    + [Что это? В чем фишка?](#%D1%87%D1%82%D0%BE-%D1%8D%D1%82%D0%BE-%D0%B2-%D1%87%D0%B5%D0%BC-%D1%84%D0%B8%D1%88%D0%BA%D0%B0)
    + [В чем отличие от cookies?](#%D0%B2-%D1%87%D0%B5%D0%BC-%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D0%B5-%D0%BE%D1%82-cookies)
    + [Что такое cookies?](#%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-cookies)
## Django

### Структура проекта

• `manage.py` - A command-line utility that allows you to interact with your Django project
• `__init__.py` - An empty file that tells Python that the current directory should be considered as a Python package
• `settings.py` - Comprises the configurations of the current project like DB connections.
• `urls.py` - All the URLs of the project are present here
• `wsgi.py` - This is an entry point for your application which is used by the web servers to serve the project you have created.

### Архитектура Django

Django следует структуре шаблона представления модели (MVT) для архитектуры, которая основана на архитектуре контроллера представления модели (MVC). В отличие от MVC, структура обрабатывает сам контроллер. Уровень модели содержит всю информацию о данных, включая как получить к нему доступ и проверить его, в то время как уровень представления помогает связать модель и шаблон.

### QuerySet

QuerySet — список объектов заданной модели. QuerySet позволяет читать данные из базы данных, фильтровать и изменять их порядок.

### Lazy Loading Django

`Count`, `len`, итерации заставляют обратиться в джанго в БД, а от других действий запроса не будет.

### Абстрактные модели

В классе meta указано abstract = true, что позволит не создавать модель в БД, а только наследоваться от нее.

### Что такое сигналы? Зачем они нужны? Назови основные?

Django включает в себя «диспетчер сигналов», который помогает разделенным приложениям получать уведомления о действиях, происходящих в других частях фреймворка. E.g. `post_delete, m2m_changed`. Они особенно полезны, когда многие части кода могут быть заинтересованы в одних и тех же событиях.

### Как реализуется связь M2M на уровне базы данных?

Обычно такие для такой связи у нас есть еще одна таблица, в которой есть ID из обоих таблиц. Напр. Клиенты и Товары.

### Что такое n + 1 проблема и как ее можно избежать в Джанго?

N + 1 Queries Problem is a performance anti-pattern that happens when a query is executed for every result you got from a previous query.

`select_related`, `prefetch_related`

### Q выражение и его использование?

Это нечто похожее на `__in`, но там можно делать фильтрацию с помощью `OR`, `AND`.

### F выражение

Вместо того, чтобы писать длинные циклы для изменения значения в колонке, мы можем написать F-выражение в одну строку, которое не будет загружать в память все значения из колонки.

### Что такое Middleware, для чего используется, как реализуется?

Middleware позволяет обрабатывать запросы из браузера, прежде чем они достигнут “view” Django, а также ответы от представлений до того, как они возвращаются в браузер. Там есть свой список из middleware. Свой можно написать в виде функции или класса.

### Назови основные middlewares и их назначение

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Опишите алгоритм работы CSRF middleware

В основе лежит следующий принцип: надо проверять, что все запросы исходят от настоящих форм с вашего сайта. 

На каждый запрос система генерирует уникальный токен и выставляет его в cookies. В каждой форме размещается скрытое поле `csrf-token` с этим же токеном. При отправке формы методом `POST` Джанго проверяет, что поле формы и значение в cookies совпадают. Если нет, это значит, что запрос подделан или отправлен с другого домена.

Чтобы освободить какую-то вьюху от проверки (если это API, например), достаточно обернуть ее декоратором `csrf_except`.

### Для чего используется класс Meta в Django models?

Можно менять поведение моделей: сделать модель абстрактной, как она будет называться (verbose_name), ordering.

### Что такое менеджеры в Django?

---

**`Manager`**  – это интерфейс, через который для моделей Django предоставляются операции запросов к базе данных. По крайней мере, один **`Manager`** существует для каждой модели в приложении Django.

Мы можем переименовать менеджер, если, например, нам нужно создать поле `objects`.

---

### Преимущества и недостатки Django ORM

| Плюсы                                                                                                                    | Минусы |
| ------------------------------------------------------------------------------------------------------------------------ | ------ |
| “Все включено”: <br> - ORM <br> - Миграции базы данных<br> - Аутентификация пользователя <br> - Панель администратора <br> | ORM развивается медленнее, чем SQLAlchemy. Active Record, который хуже, чем шаблон Unit of Work у SQLA. |
| Безопасный. Включает механизмы предотвращения распространенных атак вроде SQL-инъекций (XSS) и подделки межсайтовых запросов (CSRF)                                                                                                                         |        |

### Разница select_related и prefetch_related

Example: `Model.objects.selected_related(’field’)get(pk=id)`

Для m2m → `prefetch_related`

Для 1-1 / FK → `select_related`

### Что такое миксины

`Mixin`— это класс, предоставляющий реализации методов для повторного использования дочерними классами. Он представляет ограниченную форму множественного наследования и родительский класс, который просто даёт функциональные возможности подклассам, не содержит состояния и не предназначен для создания экземпляров.

`LoginRequiredMixin` – миксин, который можно закинуть в наследуемые объекты во вьюшку, чтобы ограничить доступ.

Одним из недостатков использования этих миксинов является то, что становится трудно анализировать, что делает класс и какие методы следует переопределить в случае, если его код слишком разбросан между несколькими классами.

### Как лучше отправлять форму GET или POST?

Форму желательно передавать методом POST по следующим причинам:

- GET-запросы могут быть кешированы, особенно в браузерах семейства IE
- GET-запросы оседают в логах провайдера, сервера, истории браузера. Пароль и логин засветиться во многих местах
- некоторые вирусы отслеживают содержимое адресной строки и пересылают третьим лицам.
- Если передаются пароли, то GET-запросы могут их в URL

> Техническое ограничение метода GET в том, что им нельзя передать файл, в отличие от POST.

### Кэширование в Django

Кэширование относится к методике сохранения выходных результатов при их первоначальной обработке, чтобы в следующий раз, когда те же результаты будут получены снова, вместо повторной обработки можно было бы использовать уже сохраненные результаты, что приводит к более быстрому доступу, а также к меньшему использованию ресурсов. Django предоставляет нам надежную систему кеширования, которая может хранить динамические веб-страницы, так что эти страницы не нужно повторно оценивать для каждого запроса.

Некоторые из стратегий кеширования в Django перечислены ниже:

- **Memcached (быстрый):** Кэш-сервер на основе памяти - самый быстрый и эффективный
- **FileSystem Caching (частый):** Значения кеша хранятся в виде отдельных файлов в сериализованном порядке.
    
**app/urls.py** 
```python
    
    **from** django.views.decorators.cache **import** cache_page
    
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    
    
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'coolsite_cache'),
        }
    }
```
    
    
- **Database Caching (редко):** Данные кеша будут храниться в базе данных и работать очень хорошо, если у вас есть быстрый и хорошо индексируемый сервер БД.
- **Local-memory Caching:** Это используется Django в качестве стратегии кеширования по умолчанию, если вы ничего не установили.

### Django Field классы

- [BinaryField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#binaryfield)
- [BooleanField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#booleanfield)
- [CharField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#charfield)
- [DateField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#datefield)
- [DateTimeField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#datetimefield)
- [DecimalField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#decimalfield)
- [EmailField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#emailfield)
- [FloatField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#floatfield)
- [IntegerField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#integerfield)
- [JSONField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield)
- [PositiveIntegerField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#positiveintegerfield)

### Объясните жизненный цикл ответа(Response lifecycle) Django?

![Untitled](django-pipeline.png)
Client → Web server (Nginx/Apache) → WSGI (gunicorn/uWSGI) → Request in middlewares → URL router → Views → Models → ORM → DB.

DB → ORM → Models → Middleware → Template | Exception → Response → WSGI → Web server → Client.

### ASGI & WSGI

**WSGI** (англ. Web Server Gateway Interface) предоставляет простой и универсальный интерфейс между большинством веб-серверов и веб-приложениями или фреймворками.

ASGI – асинхронная настройка над WSGI.

### Что такое функция django.shortcuts.render?

Объединяет заданный шаблон с заданным контекстным словарем и возвращает объект HttpResponse с этим визуализированным кодом.

Базовый синтаксис:

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

- **request**- это параметр, который генерирует ответ.
- **template_name** - это используемый HTML-шаблон
- **context**- это данные, переданные на страницу

Вы также можете указать тип контента (**content_type**), статус переданных вами данных (**status**) и возвращаемый рендер (**using**).

### Как использовать файловые сессии?

Чтобы использовать то же самое, вам необходимо установить для параметра `SESSION_ENGINE` значение `django.contrib.sessions.backends.file`.

### Разница между Django OneToOneField и ForeignKey Field

Единственное различие между ними состоит в том, что поле **ForeignKey состоит из опции on_delete** вместе с классом модели, потому что оно **используется для отношений многие к одному**, в то время как, с другой стороны, **OneToOneField выполняет только отношения один к одному** и требует только класс модели.

### Как получить SQL-запрос из набора запросов?

```python
print(queryset.query)
```

### Как можно объединить несколько QuerySet в вьюшках?

Первоначально считалось, что объединение QuerySets в списки является самым простым подходом. Вот пример того, как это сделать:

```python
result_list = list(chain(model1_list, model2_list, model3_list))
```

## DRF

DRF — это библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта.

API DRF состоит из 3-х слоев: serializers, views(viewset), urls (routers).

**`Serializer`**: преобразует информацию, хранящуюся в базе данных и определенную с помощью моделей Django, в формат, который легко и эффективно передается через API.

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```

**`Viewset`**: определяет функции (чтение, создание, обновление, удаление), которые будут доступны через API.

```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

**`Routers`**: определяет URL-адреса, которые будут предоставлять доступ к каждому виду.

```python
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

### DRF методы построения API

- APIView → самому писать все методы (CRUD) и делать кастом
- GenereicAPIView → += какое-то действие над моделью
- Viewset → для CRUD (create, read, update, delete),

> В общем случае надо использовать viewsets, потому что дает сразу больше функционала.


### Serializer в DRF

Serializer преобразует информацию, хранящуюся в базе данных и определенную с помощью моделей Django, в формат, который легко и эффективно передается через API.

Модели Django интуитивно представляют данные, хранящиеся в базе, но API должен передавать информацию в менее сложной структуре. Хотя данные будут представлены как экземпляры классов Model, их необходимо перевести в формат JSON для передачи через API.

Сериализатор DRF производит это преобразование. Когда пользователь передает информацию (например, создание нового экземпляра) через API, сериализатор берет данные, проверяет их и преобразует в нечто, что Django может сложить в экземпляр модели. Аналогичным образом, когда пользователь обращается к информации через API, соответствующие экземпляры передаются в сериализатор, который преобразовывает их в формат, который может быть легко передан пользователю как JSON.

Наиболее распространенной формой, которую принимает сериализатор DRF, является тот, который привязан непосредственно к модели Django:

```python
class ThingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thing
    fields = (‘name’, )
```

Настройки fields позволяют точно указать, какие поля доступны этому сериализатору. В качестве альтернативы, может быть установлен exclude вместо fields, которое будет включать все поля модели, кроме тех, которые указаны в exclude.

### Для чего используется класс Meta в Django serializer?

Класс Meta позволяет указать модель для сериализации и поля, включаемые в сериализацию. Все поля модели будут включены, если не задан атрибут fields.

### Система аутентификации в Django

Django поставляется со встроенной системой аутентификации пользователей, которая обрабатывает такие объекты, как пользователи, группы, разрешения пользователей и несколько пользовательских сеансов на основе файлов cookie. **Django User authentication** не только аутентифицирует пользователя, но и авторизует его.

Система состоит и работает на следующих объектах:

- **Users** (Пользователи)
- **Permissions** (Разрешения)
- **Groups** (Группы)
- **Password Hashing System** (Система хеширования паролей)
- **Forms Validation** (Проверка форм)
- **A pluggable backend system** (Подключаемая бэкэнд-система)

### DRF permissions

…

## Flask

### Django vs Flask

Фласк меньше идет из коробки и больше подходит для микросервисом, а в джанго большое количество методов / инструментов прямо из коробки.

### Что быстрее Flask или Django и почему?

В Django больше слоев и больше фичей из коробки, поэтому он медленнее.

![Untitled](django-flask.png)

---

## FastAPI

### Почему  FastAPI?

Асинхронность

Аннотации типов, pydantic

Недостатки в медленном развитии самого фреймворка и сопутствующих библиотек.

---

### миграции alembic

### related модели sqlalchemy

---

## JWT

### Что это? В чем фишка?

1) шифрует

### В чем отличие от cookies?

### Что такое cookies?