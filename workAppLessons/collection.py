# Модуль collections - предоставляет специализированные типы данных,
# на основе словарей, кортежей, множеств, списков.
# Первым рассматриваемым типом данных будет Counter.

#                   collections.Counter
# Наиболее часто употребляемые шаблоны для работы с Counter:
#     sum(c.values()) - общее количество.
#     c.clear() - очистить счётчик.
#     list(c) - список уникальных элементов.
#     set(c) - преобразовать в множество.
#     dict(c) - преобразовать в словарь.
#     c.most_common()[:-n:-1] - n наименее часто встречающихся элементов.
#     c += Counter() - удалить элементы, встречающиеся менее одного раза.

#                   collections.deque
# collections.deque(iterable, [maxlen]) - создаёт очередь из итерируемого объекта
# с максимальной длиной maxlen. Очереди очень похожи на списки, за исключением того,
# что добавлять и удалять элементы можно либо справа, либо слева.
# Методы, определённые в deque:
#   append(x) - добавляет x в конец.
#   appendleft(x) - добавляет x в начало.
#   clear() - очищает очередь.
#   count(x) - количество элементов, равных x.
#   extend(iterable) - добавляет в конец все элементы iterable.
#   extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).
#   pop() - удаляет и возвращает последний элемент очереди.
#   popleft() - удаляет и возвращает первый элемент очереди.
#   remove(value) - удаляет первое вхождение value.
#   reverse() - разворачивает очередь.
#   rotate(n) - последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).

# collections.Counter - вид словаря, который позволяет нам считать
# количество неизменяемых объектов (в большинстве случаев, строк). Пример:
import collections
# Counter = collections.Counter()
print('#/////////  (1)  ///////////#')

c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1
print(c)
print(c['spam'])
print(c['counter'])
# ////////////////////////////////////
print('#/////////  (2)  ///////////#')
# Но возможности Counter на этом не заканчиваются. У него есть несколько специальных методов:
# elements() - возвращает список элементов в лексикографическом порядке.
c = collections.Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))
# ////////////////////////////////////
print('#/////////  (3)  ///////////#')
# most_common([n]) - возвращает n наиболее часто встречающихся элементов, в порядке убывания
# встречаемости. Если n не указано, возвращаются все элементы.
print(collections.Counter('abracadabra').most_common(5))
# ////////////////////////////////////
print('#/////////  (4)  ///////////#')
# subtract([iterable-or-mapping]) - вычитание
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
print(c.subtract(d))
print(c + d)
print(c & d)
print(c | d)
# ////////////////////////////////////
print('#/////////  (5)  ///////////#')
# collections.defaultdict
# collections.defaultdict ничем не отличается от обычного словаря за исключением того,
# что по умолчанию всегда вызывается функция, возвращающая значение:
defdict = collections.defaultdict(list)
print(defdict)
for i in range(6):
    defdict[i].append(i)
print(defdict)
# ////////////////////////////////////
print('#/////////  (6)  ///////////#')
# collections.OrderedDict
# collections.OrderedDict - ещё один похожий на словарь объект, но он помнит порядок,
# в котором ему были даны ключи. Методы:
#   popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.
#   move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(collections.OrderedDict(sorted(d.items(), key=lambda t: t[0])))
print(collections.OrderedDict(sorted(d.items(), key=lambda t: t[1])))
print(collections.OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))
# ////////////////////////////////////
print('#/////////  (7)  ///////////#')
# collections.namedtuple()
# Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением,
# что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ:
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p)
print(p.x)
print(p[1])