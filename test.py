import random
import queue

if __name__ == '__main__':
    queue = [1, 2, 3, 4, 5]
    queue.append(6)
    queue.pop(0)
    print(queue)

    stack = [1, 2, 3, 4]
    stack.pop()
    stack.append(5)
    print(stack)
