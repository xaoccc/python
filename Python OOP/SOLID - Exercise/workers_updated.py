from abc import ABC, abstractmethod
import time


class WorkingWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class EatingWorker(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(WorkingWorker, EatingWorker):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(2 secs)")
        time.sleep(2)


class SuperWorker(WorkingWorker, EatingWorker):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(WorkingWorker):
    def work(self):
        print("I'm a robot. I'm working....")


class GliganPeshev(EatingWorker):
    def eat(self):
        print("I was a star in a TV reality show and i can eat 25 cakes for 5 minutes")


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass

class WorkManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, WorkingWorker):
            raise AssertionError (f"`worker` must be of type {WorkingWorker}")
        self.worker = worker

    def manage(self):
        self.worker.work()


class EatManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, EatingWorker):
            raise AssertionError (f"`worker` must be of type {EatingWorker}")
        self.worker = worker

    def manage(self):
        self.worker.eat()



manager = WorkManager()
makdonald = EatManager()
manager.set_worker(Worker())
manager.manage()
makdonald.set_worker(GliganPeshev())
makdonald.manage()
makdonald.set_worker(Worker())
makdonald.manage()
makdonald.manage()

manager.set_worker(SuperWorker())
manager.manage()


manager.set_worker(Robot())
manager.manage()

