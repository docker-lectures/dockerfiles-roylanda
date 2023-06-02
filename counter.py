import time

def count(): 
    c = 0
    while True: 
        c = c + 2 
        print(f"count {c}")
        time.sleep(0.5)


if __name__ == "__main__": 
    count()