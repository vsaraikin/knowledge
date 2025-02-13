# System Design

[GitHub - donnemartin/system-design-primer: Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards.](https://github.com/donnemartin/system-design-primer)

Главная идея – задавать вопросы.
1.  Что точно должна уметь делать система (сколько предметов влезает в коробку, каковы они по размерам)?
2. Формат системы? Веб/мобилка/дестктоп?
3. Вопросы по функциональность. Что должно быть? Какие главные возможности?
4. Если лента, то подумать, как это сортировать новости.
5. Какие будут файлы? Сколько они будут весить? Что за формат данных в системе будет?
6. Сколько пользователей будет? Какой объем трафика? 
7. Storage сколько? Что мы должны хранить?
8. Сколько запросов будем обрабатывать? Load balance?
9. Шифрование?
10. Мне надо проектировать эндпоинты?
11. Спросить интервьюера, а что он думает?

Общий вид схемы

Шаг 1. Понять задачу и определить масштаб: 3–10 минут.  Спросить про функциональные требования (какие кнопочки). Спросить про НФТ (что хотелось бы)
  
Шаг 2. Предложить общее решение и получить одобрение: 10–15 минут.  
  
Шаг 3. Подробное проектирование: 10–25 минут.  
  
Шаг 4. Подведение итогов: 3–5 минут.

Вспомнить виды БД и способы их масштибарования.

Кэширование, вертикальное и горизонтальное масштабирование
![operation-speed](operation-speed.png)