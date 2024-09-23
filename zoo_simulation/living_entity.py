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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
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
        return f'{self.__class__.__name__} {self.name} {"♂️" if self.sex == Sex.MALE else "♀️"}'

    @abstractmethod
    def can_eat(self, other_living_entity):
        """
        Method to check if animal can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return False

    @abstractmethod
    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        pass


class Carnivorous(Animal):
    """
    An abstract class to represent a Carnivorous animal

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """

    def can_eat(self, other_living_entity):
        """
        Method to check if animal can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Animal)


class Lion(Carnivorous):
    """
    A class to represent a Lion

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """

    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🦁 " + super().__repr__()


class Tiger(Carnivorous):
    """
    A class to represent a Tiger

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """

    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🐅 " + super().__repr__()


class Coyote(Carnivorous):
    """
    A class to represent a Coyote

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """
    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🦊 " + super().__repr__()


class Herbivore(Animal):
    """
    An abstract class to represent a Herbivore animal

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only Plant)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """

    def can_eat(self, other_living_entity):
        """
        Method to check if animal can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Plant)


class Elephant(Herbivore):
    """
    A class to represent an Elephant

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """
    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🐘 " + super().__repr__()


class Giraffe(Herbivore):
    """
    A class to represent a Giraffe

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """
    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🦒 " + super().__repr__()


class Antelope(Herbivore):
    """
    A class to represent an Antelope

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

    can_eat(self, other_living_entity):
        Method to check if animal can eat other living_entity (only other Animal)

    eat(self, other_living_entity):
        Method to allow animal to eat (need to be implemented in subclasses)
    """
    def eat(self, other_living_entity):
        """
        Method to allow animal to eat

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that current animal will eat

        Returns
        -------
        None
        """
        if self.can_eat(other_living_entity):
            print(f"{self} eat {other_living_entity}")

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "𓃴 " + super().__repr__()


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
        return "🌿 Plant"
