from abc import ABC, abstractmethod
from enum import Enum
from random import shuffle


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
    _is_alive : True if LivingEntity is alive, False is LivingEntity is dead

    Methods
    -------
    __repr__(self):
        Abstact method (need to be implemented in subclasses)

    do_actions(self, other_living_entity)
        Do action(s) for the current living entity (need to be implemented in subclasses)

    is_alive:
        Getter for _is_alive attribute

    gets_eaten(self):
        Method called when LivingEntity has been eaten
    """

    def __init__(self) -> None:
        """
        Empty constructor for LivingEntity
        """
        self._is_alive = True

    @abstractmethod
    def __repr__(self) -> str:
        """
        Return a string representation of the object
        (need to be implemented in subclasses)
        """
        return ""

    @abstractmethod
    def do_actions(self, other_living_entity) -> None:
        """
        Do action(s) for the current living entity
        (need to be implemented in subclasses)
        """
        pass

    @property
    def is_alive(self):
        """
        Getter for _is_alive attribute
        """
        return self._is_alive

    def gets_eaten(self) -> None:
        """
        Method called when the LivingEntity has been eaten
        """
        self._is_alive = False


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

    do_actions(self, other_living_entity)
        Do action(s) for the current animal

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
        return f'{self.__class__.__name__} {self.name} {"♂️" if self.sex == Sex.MALE else "♀️"} {"❤️" if self.is_alive else "💀"}'

    def do_actions(self, other_living_entity) -> None:
        """
        Do action(s) for the current animal
        """
        # Only if the animal is alive
        if self.is_alive:
            # The animal needs to eat a plant or an another animal
            living_entities = [le for le in other_living_entity if le.is_alive]
            shuffle(living_entities)
            has_already_eaten = False
            while not has_already_eaten and len(living_entities):
                another_living_entity = living_entities.pop()
                if self.can_eat(another_living_entity):
                    self.eat(another_living_entity)
                    has_already_eaten = True

            if not has_already_eaten:
                print(f"{self} couldn't eat :'(")

    @abstractmethod
    def can_eat(self, other_living_entity) -> bool:
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

    def eat(self, other_living_entity) -> None:
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
            other_living_entity.gets_eaten()
            print(f"{self} eat {other_living_entity}")


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

    @abstractmethod
    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Carnivorous can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return False


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

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Lion can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Animal) and \
            self != other_living_entity and \
            other_living_entity.is_alive and \
            not isinstance(other_living_entity, Lion)

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

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Tiger can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Animal) and \
            self != other_living_entity and \
            other_living_entity.is_alive and \
            not isinstance(other_living_entity, Tiger)

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

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Coyote can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Animal) and \
            self != other_living_entity and \
            other_living_entity.is_alive and \
            not isinstance(other_living_entity, Coyote)

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

    @abstractmethod
    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Carnivorous can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return False


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

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🐘 " + super().__repr__()

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Elephant can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Plant) and other_living_entity.is_alive


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

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "🦒 " + super().__repr__()

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Giraffe can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Plant) and other_living_entity.is_alive


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

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return "𓃴 " + super().__repr__()

    def can_eat(self, other_living_entity) -> bool:
        """
        Method to check if Antelope can eat other living_entity

        Parameters
        ----------
        other_living_entity : other LivingEntity
            that we will to check the eatability

        Returns
        -------
        True or False
        """
        return isinstance(other_living_entity, Plant) and other_living_entity.is_alive


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

    do_actions(self, other_living_entity)
        Do action(s) for the current plant

    """
    def __init__(self) -> None:
        """
        Construct all the necessary attributes for the Plant object.
        """
        super().__init__()

    def do_actions(self, other_living_entity) -> None:
        """
        Do action(s) for the current Plant
        """
        pass  # No action for plant for the moment

    def __repr__(self) -> str:
        """
        Return a string
        """
        return f"""🌿 Plant {"❤️" if self.is_alive else "💀"}"""
