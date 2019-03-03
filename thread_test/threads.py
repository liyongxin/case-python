# -*- coding: utf-8 -*-
import threading
from thread_test.collector.collector import Collector

class GrabThread(threading.Thread):

    def __init__(self,func,args=()):
        super(GrabThread,self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def get_all_subclasses(mod):
    all_subclasses = {}
    ## collections
    for subclass in mod.__subclasses__():
        class_name = subclass.__name__.lower()
        if not class_name in all_subclasses.keys():
            all_subclasses[class_name] = subclass
        get_all_subclasses(subclass)
    return all_subclasses


def main():
    all_cls = get_all_subclasses(Collector)
    threads = []
    for item, value in all_cls.items():
        fn_collect = getattr(value, 'get_data', None)
        if callable(fn_collect):
            p = GrabThread(func=fn_collect, args=(item,))
            threads.append(p)
            p.start()
            print("执行{0}的collect 方法".format(item))
    for p in threads:
        p.join()  #

    print("main done")

if __name__ == '__main__':
    main()