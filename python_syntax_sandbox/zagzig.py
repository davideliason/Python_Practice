import time,sys

indent = 0 #globa

# main loop
while True:
    try:
        print(" " * indent,end="")
        print("#####")
        time.sleep(0.1)
        indent += 1

    except KeyboardInterrupt:
        sys.exit()
