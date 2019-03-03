# -*- coding: utf-8 -*-
from multiprocessing import Manager, Process
from thread_test.collector.collector import Collector


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
    manager = Manager()
    results = manager.dict()  # 多进程共享数据
    processes = []  # 进程id
    for item, value in all_cls.items():
        fn_collect = getattr(value, 'grab', None)
        if callable(fn_collect):
            p = Process(target=fn_collect, name=item, args=(item, results))
            processes.append(p)
            p.start()
            print("执行{0}的collect 方法".format(item))
    for p in processes:
        p.join()  #
    print("main done")

if __name__ == '__main__':
    main()