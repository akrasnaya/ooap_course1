class Deque:

    # КОНСТРУКТОР
    def __init__(self):
        self.dequeue = []
    # post-condition - создана пустая очередь

    # КОМАНДЫ

    def add_back(self, value):
    # post-condition - в хвост добавлен новый элемент со значением value

    def add_front(self, value):
    # post-condition - в голову добавлен новый элемент со значением value

    def delete_back(self):
    # pre-condition - очередь не пустая
    # post-condition - удален первый элемент очереди

    def delete_front(self):
    # pre-condition - очередь не пустая
    # post-condition - удален первый элемент очереди

    # ЗАПРОСЫ

    def size(self):  # текущий размер очереди


    # ЗАПРОСЫ СТАТУСОВ

    def get_queue_status(self):  # успешно - элемент добавлен
    def get_deque_status(self):  # успешно - элемент удален