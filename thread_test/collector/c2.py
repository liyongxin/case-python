from .collector import Collector

class C2(Collector):

    @classmethod
    def get_data(cls, msg):
        print("i am from ", msg)