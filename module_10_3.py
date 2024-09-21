from random import randint
import  time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            #нужно открыть замок
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            numb_ = randint(50,500)
            self.balance += numb_
            print(f"Пополнение: {numb_}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            #нужно закрыть замок
            num_ = randint(50, 500)
            print(f"Запрос на {num_}")
            if num_ <= self.balance:
                self.balance -= num_
                print(f"Снятие: {num_}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

# a = Bank(100,2)
# a.deposit()
# a.take()
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
