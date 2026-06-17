from abc import ABC,abstractmethod
class finding_area(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(finding_area):
    def __init__    