import time

import multiprocessing

# Define a new function that wait 1 second
def sleepy_man():
    print("Starting to sleep")
    time.sleep(1)
    print("Done sleeping")


if __name__ == "__main__":

    # Get current time before script's execution
    tic: float = time.time()

    # Instantiate two new process
    p1: multiprocessing.Process = multiprocessing.Process(target = sleepy_man)
    p2: multiprocessing.Process = multiprocessing.Process(target = sleepy_man)

    # Start both new process
    p1.start()
    p2.start()

    # Wait for both process to end
    p1.join()
    p2.join()

    # get current time after script's execution
    toc: float = time.time()

    # Compite elapsed time
    time_elapsed: float = toc - tic

    # Print elapsed time
    print(f"\n{time_elapsed = }\n")