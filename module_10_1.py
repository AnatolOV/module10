import time
from datetime import  datetime
from threading import Thread

def write_words(word_count, file_name):
    # time_start = datetime.now()
    # print(time_start)
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f"Какое-то слово № {i}\n")

    # time_stop = datetime.now()
    # time_last = time_stop - time_start
    print(f"Завершилась запись в файл {file_name}")
    # print(f'Работа потоков {time_last}')

data_ = [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]
time_start = datetime.now()
for i in data_:
    write_words(i[0],i[1])

time_stop = datetime.now()
time_last = time_stop - time_start
print(f'Работа потоков {time_last}')

time_start2 = datetime.now()

first_thread = Thread(target=write_words, args=(10,'example5.txt'))
second_thread = Thread(target=write_words, args=(30,'example6.txt'))
third_thread = Thread(target=write_words, args=(200,'example7.txt'))
fours_thread = Thread(target=write_words, args=(100,'example8.txt'))

first_thread.start()
second_thread.start()
third_thread.start()
fours_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fours_thread.join()


time_stop2 = datetime.now()
time_last2 = time_stop2 - time_start2
print(f'Работа потоков {time_last2}')