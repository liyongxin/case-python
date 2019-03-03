import sys, os
print(sys.path)
from thread_test.threads import get_all_subclasses
from thread_test.collector.collector import Collector

if __name__ == '__main__':
    print(123)

    print(os.path.dirname(os.path.abspath(__file__)))
    print(sys.path)
    print(get_all_subclasses(Collector))