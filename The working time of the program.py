import time

start_time = time.time()

# for example
for i in range(5): 
    print(i)
    time.sleep(1)

end_time = time.time()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')
