"""
Implement a simple queue using a list
"""
class Queue:
    def __init__(self, queue = None):
        self.queue = queue if queue else []

    def remove(self):
        return self.queue.pop(0)
    
    def add(self, item):
        self.queue.append(item)

    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

def main():
    # test the queue class
    queue = Queue()
    queue.add(5)
    queue.add(10)
    print(queue.remove())
    print(queue.remove())


if __name__ == '__main__':
    main()