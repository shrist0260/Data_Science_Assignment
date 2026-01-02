#Queue using library 
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print("Queue:", queue)
print("Depueued:", queue.popleft())