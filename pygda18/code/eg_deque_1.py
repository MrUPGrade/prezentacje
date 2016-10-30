from collections import deque
from datetime import datetime

q = deque(maxlen=2)

for i in range(1, 11):
    log = '%s: It happened %s time(s)' % (datetime.utcnow(), i)
    q.append(log)

print(q)
