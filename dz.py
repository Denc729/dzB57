import time


def time_this(func):
    def wrap():
        list_time=[]
        for i in range(10):
              
            t1=time.time()
            func()
            t2=time.time()
            list_time.append(t2-t1)
            print("Выполнение функции - {0}".format(t2-t1))
        midle_time=sum(list_time)/len(list_time)
        print("Среднее время выполнения - {0}".format(midle_time))
    return wrap






@time_this
def fib():  
    fib_list=[1,2]
    for i in range(100000):
        fib_list.append(fib_list[-1]+fib_list[-2])
        
    



fib()