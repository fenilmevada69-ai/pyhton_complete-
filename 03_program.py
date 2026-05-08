#implement an exponential backoff strategy that doubles the wait time between retries, starting from 1s, but stops after 5 retries
import time

wait_time = 1
max_retrives = 5
attempts = 0

while attempts < max_retrives:
    print(f"Attempt: {attempts+1}, wait_time: {wait_time}s")
    if(attempts == 4):
        break
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1