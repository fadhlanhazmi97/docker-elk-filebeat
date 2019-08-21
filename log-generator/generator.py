import time

f1 = open("raw.log","r")
lines = f1.readlines()
count = 8
f2 = open("uwsgi.log","a",buffering=1)
try:
    while True:
        for line in lines:
            f2.write(line)
            print(line)
            time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
    f1.close()
    f2.close()