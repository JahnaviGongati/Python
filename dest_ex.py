#import time
class test:
    def __init__(self):
        print("Object initialization")
    def __del__(self):
        print("Fulfilling  last wish and performing clean up activities")
t1=test()
t1=None
#time.sleep(5)
print("End of application")
