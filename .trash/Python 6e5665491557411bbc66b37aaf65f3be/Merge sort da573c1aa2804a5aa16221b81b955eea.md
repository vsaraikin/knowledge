# Merge sort

Answer: 1. Список делится пополам. Если нечетная длина, то меньшая в начале и большая в конце.
2. Рекурсивно вызываем пока в разделенном массиве будет только один элемент.
3. Дальше эти листы с одним элементом начинаем соединять до тех пор пока не соединим все списки снизу вверх.

Python uses Timosort — derived from merge sort and insertion sort

best case: O(n*log(n))
worst case: O(n*log(n))
Type: Algos
URL: https://www.youtube.com/watch?v=LCfwxi2RPK4