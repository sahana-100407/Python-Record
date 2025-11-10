from collections import Counter

counts = Counter(['a', 'b', 'a', 'c', 'b'])
print(counts)

from collections import deque
d = deque([1, 2, 3])
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x)

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
