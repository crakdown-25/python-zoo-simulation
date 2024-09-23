from abc import ABC, abstractmethod
from enum import Enum
from random import shuffle, randint

PV_LOSTS_ANIMAL_BY_DAY = 1
PV_LOSTS_ANIMAL_WHEN_EATEN = 4
PV_OBTAINED_CARNIVOROUS_BY_ANIMAL = 5

LIMIT_PV_BEFORE_EATEN = 5

PV_OBTAINED_PLANT_BY_DAY = 1
PV_LOSTS_PLANT_WHEN_EATEN = 2
PV_OBTAINED_HERBIVORE_BY_PLANT = 3

MIN_AGE_FOR_ENTITY_ADDED = 0
MAX_AGE_FOR_ENTITY_ADDED = 19
DEATHING_AGE_IN_DEAY = 20
STANDARD_AGE_FOR_TEST = 12


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
    _life_point : Number of life point (PV) for this LivingEntity
    _age : LivingEntity age

    Methods
    -------
    grow_old(self):
        Method called when the LivingEntity grow_old

    __repr__(self):
        Abstact method (need to be implemented in subclasses)

    do_actions(self, other_living_entity):
        Do action(s) for the current living entity (need to be implemented in subclasses)

    is_alive:
        Getter for _is_alive attribute

    life_point:
        Getter for _life_point attribute

    age:
        Getter for _age attribute

    gets_eaten(self):
        Method called when the LivingEntity has been eaten. Return PV to add to eater
        (need to be implemented in subclasses)

    check_PV(self):
        Return True is _life_point is >1, False otherwise (in this case self._is_alive is set to False too)
    """
    testing_mode = False  # Class variable we set to True (during test) to obtain reproducible behaviors

    def __init__(self, age) -> None:
        """
        Constructor for LivingEntity
        """
        self._is_alive = True
        self._life_point = 10
        if age:
            self._age = age
        else:
            self._age = STANDARD_AGE_FOR_TEST if self.testing_mode else randint(MIN_AGE_FOR_ENTITY_ADDED, MAX_AGE_FOR_ENTITY_ADDED)

    def grow_old(self) -> None:
        """
        Method called when the LivingEntity grow_old. If LivingEntity's age >= DEATHING_AGE_IN_DEAY, the LivingEntity will dead
        """
        self._age += 1
        if self._age >= DEATHING_AGE_IN_DEAY:
            self._is_alive = False

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

    @property
    def life_point(self):
        """
        Getter for _life_point attribute
        """
        return self._life_point

    @property
    def age(self):
        """
        Getter for _age attribute
        """
        return self._age

    @abstractmethod
    def gets_eaten(self) -> int:
        """
        Method called when the LivingEntity has been eaten. Return PV to add to eater
        (need to be implemented in subclasses)
        """
        return 0

    def check_PV(self) -> bool:
        """
        Return True is _life_point is >1, False otherwise (in this case self._is_alive is set to False too)
        """
        if self._life_point <= 0:
            self._is_alive = False
            return False
        else:
            return True


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

    def __init__(self, name: str, sex: Sex, age=None) -> None:
        """
        Construct all the necessary attributes for the animal object.

        Parameters
        ----------
            name : str
                the name of the animal
            sex : Sex (MALE/FEMALE)
                sex of the animal
        """
        super().__init__(age=age)
        self.name = name
        self.sex = sex

    def __repr__(self) -> str:
        """
        Return a string representation of the animal
        """
        return f'{self.__class__.__name__} {self.name} {"♂️" if self.sex == Sex.MALE else "♀️"} PV {self._life_point} Age {self._age} {"❤️" if self.is_alive else "💀"}'

    def do_actions(self, other_living_entity) -> None:
        """
        Do action(s) for the current animal
        """
        # Only if the animal is alive
        if self.is_alive:
            # First, the animal grow old
            self.grow_old()
            # If the animal is always alive
            if self.is_alive:
                # First, the animal losts PV_LOSTS_ANIMAL_BY_DAY (1) PV
                self._life_point -= PV_LOSTS_ANIMAL_BY_DAY
                # Check PV and continue process only if animal is alive
                if self.check_PV():
                    if self._life_point <= LIMIT_PV_BEFORE_EATEN:

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
            self._life_point += other_living_entity.gets_eaten()
            print(f"{self} eat {other_living_entity}")

    def gets_eaten(self) -> int:
        """
        Method called when the Animal has been eaten. Return PV to add to eater
        """
        self._life_point -= PV_LOSTS_ANIMAL_WHEN_EATEN
        self.check_PV()
        return PV_OBTAINED_CARNIVOROUS_BY_ANIMAL


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

    gets_eaten(self)
        Method called when the Plant has been eaten. Return PV to add to eater

    """
    def __init__(self, age=None) -> None:
        """
        Construct all the necessary attributes for the Plant object.
        """
        super().__init__(age=age)

    def do_actions(self, other_living_entity) -> None:
        """
        Do action(s) for the current Plant
        """
        if self.is_alive:
            # Plant grow old
            self.grow_old()
            # If plant is always alive
            if self.is_alive:
                # Plant get PV_OBTAINED_PLANT_BY_DAY (1) PV per day
                self._life_point += PV_OBTAINED_PLANT_BY_DAY

    def gets_eaten(self) -> int:
        """
        Method called when the Plant has been eaten. Return PV to add to eater
        """
        self._life_point -= PV_LOSTS_PLANT_WHEN_EATEN
        self.check_PV()
        return PV_OBTAINED_HERBIVORE_BY_PLANT

    def __repr__(self) -> str:
        """
        Return a string
        """
        return f"""🌿 Plant PV {self._life_point} Age {self._age} {"❤️" if self.is_alive else "💀"}"""
