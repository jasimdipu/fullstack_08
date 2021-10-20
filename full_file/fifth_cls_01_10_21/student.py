# abstraction
from abc import ABC, abstractmethod, abstractproperty


class Student(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getDept(self):
        pass

    @abstractmethod
    def setDept(self, dept):
        pass
