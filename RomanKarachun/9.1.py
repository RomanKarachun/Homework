import threading
import time
class hw_9_1(threading.Thread):
    running = True
    def __init__(self, index, left, right):
        threading.Thread.__init__(self)
        self.index = index
        self.left = left
        self.right = right
    def dinner(self):
        fork1, fork2 = self.left, self.right
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False) 
            if locked:
                break
            fork1.release()
            print ("%s swaps forks \n" % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()
    def run(self):
        while(self.running):
            time.sleep(2)
            print ("%s is hungry \n" % self.index)
            self.dinner()
    def dining(self):			
        print ("%s eats \n" % self.index)
        time.sleep(2)
        print ("%s leaves to think \n" % self.index)
def main():
    forks = [threading.Semaphore() for n in range(5)]
    philosophers= [hw_9_1(i, forks[i%5], forks[(i+1)%5]) for i in range(5)]
    hw_9_1.running = True
    for p in philosophers:
        p.start()
    time.sleep(5)
    hw_9_1.running = False
if __name__ == "__main__":
    main()
