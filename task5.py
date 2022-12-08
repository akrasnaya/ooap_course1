class Queue:

    # КОНСТРУКТОР
    def __init__(self):
        self.queue = []
    # post-condition - создана пустая очередь

    # КОМАНДЫ

    def enqueue(self, value):
    # post-condition - в хвост добавлен новый элемент со значением value

    def dequeue(self):
    # pre-condition - очередь не пустая
    # post-condition - удален первый элемент очереди

    # ЗАПРОСЫ

    def size(self): # текущий размер очереди

    def get_head(self): # получение первого элемента очереди
    # pre-condition - очередь не пустая

    # ЗАПРОСЫ СТАТУСОВ

    def get_queue_status(self): # успешно - элемент добавлен
    def get_deque_status(self): # успешно - элемент удален
