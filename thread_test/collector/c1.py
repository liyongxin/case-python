from .collector import Collector

class C1(Collector):

    @classmethod
    def get_data(cls, msg):
        print("i am from ", msg)