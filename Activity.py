# import necessery modules
from abc import ABC,abstractmethod

# create base class
class abclass(ABC):
    def print(self,x):
        print(f"the value is {x}")
    # abstract method
    @abstractmethod
    def task(self):
        print("We are inside the abclass task")
# create subclass
class testclass(abclass):
     def task(self):
        print("We are inside the testclasslass task")
obj=testclass()
obj.task()
obj.print(6)