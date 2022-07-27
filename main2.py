import sys
import multiprocessing
from subprocess import call

def notify(path):
    
        
    def call_python_file(path):
            
        call(["pythonw" , "{}".format(path)]) 
             
    call_python_file(path)



p1 = multiprocessing.Process(target=notify , args=["D:\\nikhil python\\eye saver\\notification.py"])
p3 = multiprocessing.Process(target=notify , args=["D:\\nikhil python\\eye saver\\facedistance2.py"])
p2 = multiprocessing.Process(target=notify , args=["D:\\nikhil python\\eye saver\\ui3.py"] )
p4 = multiprocessing.Process(target=notify , args = ["D:\\nikhil python\\eye saver\\blink2.py"])

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    sys.exit()
