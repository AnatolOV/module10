import time
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        start = time.time()
        data = file.readlines()
        for line in data:
            if line != '':
                all_data.append(line.strip())
        stop = time.time()
        duration = stop - start
        print(duration)
    # print(all_data)


list_files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
for file in list_files:
    read_info(file)


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(read_info,list_files)