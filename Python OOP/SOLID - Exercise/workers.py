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


class BobiTurboto(TheWorker):
    def work(self):
        print("Dai 6000 marki!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, TheWorker):
            raise AssertionError(f'`worker` must be of type {TheWorker}')
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
super_worker = SuperWorker()
bobi = BobiTurboto()
manager = Manager()
manager.set_worker(worker)
manager.manage()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support non-worker type of person")
manager.manage()
manager.set_worker(bobi)
manager.manage()