from abc import ABC, abstractmethod


class TheWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(TheWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(TheWorker):
    def work(self):
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    @property
    def worker(self):
        return self.__worker

    @worker.setter
    def worker(self, value):
        if not isinstance(value, Worker):
            raise AssertionError(f'`worker` must be of type {TheWorker}')
        self.__worker = value





    def manage(self):
        if self.worker is not None:
            self.worker.work()





worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
