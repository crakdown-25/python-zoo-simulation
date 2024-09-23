from abc import ABC, abstractmethod
from enum import Enum


class Sex(Enum):
    """
    Enumeration class to manage animals' sex
    """
    MALE = 1
    FEMALE = 2


class LivingEntity(ABC):
    """
    An abstract class to represent a living entity.

    ...

    Attributes
    ----------

    Methods
    -------
    __repr__(self):
        Abstact method (need to be implemented in subclasses)
    """

    def __init__(self) -> None:
        """
        Empty constructor for LivingEntity
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Return a string representation of the object
        (need to be implemented in subclasses)
        """
        return ""


class Animal(LivingEntity):
    """
    A class to represent an Animal

    ...

    Attributes
    ----------
    name : str
        the name of the animal
    sex : Sex (MALE/FEMALE)
        sex of the animal

    Methods
    -------
    __repr__(self):
        Return a string to describe the current animal
    """

    def __init__(self, name: str, sex: Sex) -> None:
        """
        Construct all the necessary attributes for the animal object.

        Parameters
        ----------
            name : str
                the name of the animal
            sex : Sex (MALE/FEMALE)
                sex of the animal
        """
        super().__init__()
        self.name = name
        self.sex = sex

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return f'Animal {self.name} {"♂️" if self.sex == Sex.MALE else "♀️"}'


class Plant(LivingEntity):
    """
    A class to represent a plant

    ...

    Attributes
    ----------

    Methods
    -------
    __repr__(self):
        Return a string to describe the current plant
    """

    def __repr__(self) -> str:
        """
        Return a string
        """
        return "A Plant"
