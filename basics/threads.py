# A thread is a separate flow of execution. 
# Tasks that spend much of their time waiting for external events are generally good candidates for threading. 

import threading
import time
import logging


def main():

    lives = 10

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO) # datefmt="%H:%M:%S")

    main_begin = time.perf_counter()

    # Option 1: Create a Thread using constructor
    # Pass it a function and a list containing the arguments to that function.
    t1 = threading.Thread(target=thread_function, args=(4,), name="task01")
    t2 = threading.Thread(target=thread_function, args=(2,), name="task02")
    
    # Start the thread’s activity:
    t1.start()  
    t2.start() 

    # while lives > 0:
    #     print("*", end="", flush=True)
    #     time.sleep(1)
    #     lives -= 1

    # Wait until the thread terminates.
    t1.join()
    t2.join()

    main_end = time.perf_counter()
    # There is a “MainThread” object; this corresponds to the initial thread of control in the Python program.
    logging.info(f"{threading.current_thread().name}    : all done in {main_end - main_begin} sec(s)") 


def thread_function(seconds):
    global lives
    # A thread has a name. The name can be passed to the constructor, and read or changed through the name attribute.
    name = threading.current_thread().name
    logging.info(f"Thread id={threading.get_ident()} {name=}: BEGIN")
    time.sleep(seconds)     # simulate workload
    lives = 0   # reset global counter for the loop
    logging.info(f"Thread {name}: END")


if __name__ == "__main__":
    main()


