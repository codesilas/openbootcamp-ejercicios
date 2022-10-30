import time

actual = time.time()
obj = time.localtime(actual)
time_string = time.asctime(obj)

# fecha = time.ctime(actual)

print(type(time_string))