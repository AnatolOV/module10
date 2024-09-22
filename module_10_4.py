from threading import Thread
from random import randint
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        pause = randint(3, 10)
        time.sleep(pause)


class Cafe:
    def __init__(self, *args):

        self.queue = queue.Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for i in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = i
                    i.start()
                    print(f"{i.name} сел(-а) за стол номер {table.number}")
                    seated = True
                    break
            if not seated:
                self.queue.put(i)
                print(f"{i.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest != None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

                    time.sleep(1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# for i in guests:
#     print(i.name)
# # Заполнение кафе столами
cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()
