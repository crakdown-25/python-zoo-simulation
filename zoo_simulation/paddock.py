import re
from .living_entity import LivingEntity, Plant, Animal, Sex


class Paddock():
    """
    A class to represent a paddock in a zoopark.

    ...

    Attributes
    ----------
    lst_living_entity : list
        List of living entity in the paddock (plant(s) / animal(s))

    Methods
    -------
    initialization
        Allow user to make initialization of the paddock

    run_simulation
        Run simulation of life in a paddock

    add_plant(plant: Plant)
        Add the plant to the paddock

    add_animal(animal: Animal)
        Add the animal to the paddock

    and_one_more_day()
        Do day's action(s) and display a report

    create_report()
        Create a report for the paddock

    """

    def __init__(self) -> None:
        """
        Construct all the necessary attributes for the paddock object.
        """
        self.lst_living_entity = []  # type: list[LivingEntity]

    def initialization(self) -> None:
        """
        Allow user to make initialization of the paddock

        Returns
        -------
        None
        """
        print("Let's start initialization step")
        pattern = r'^[Pp][Ll][Aa][Nn][Tt] (\d+)$'
        continue_initialization = True
        while continue_initialization:
            print("Enter 'Plant' to add a plant")
            print("Enter 'Plant X (X : a positive integer)' to add X plants")
            print("Enter 'Animal animal_name m/f' to add an animal")
            print("Enter 'q' to stop initilization step")
            answer = input()
            match answer.lower():
                case "q":
                    continue_initialization = False
                case "plant":
                    self.add_plant(Plant())
                    print("One plant added\n")
                case _:
                    if len(infos := answer.split(" ")) == 3 and \
                            infos[0].lower() == 'animal' and \
                            infos[2].lower() in ['m', 'f']:
                        animal = Animal(infos[1], Sex.MALE if infos[2].lower() == 'm' else Sex.FEMALE)
                        self.add_animal(animal)
                        print(f"Animal {animal.name} added\n")
                    elif result := re.match(pattern, answer):
                        nb_plants_to_add = int(result.group(1))
                        for p in range(nb_plants_to_add):
                            self.add_plant(Plant())
                        print(f"{nb_plants_to_add} plant(s) added\n")
                    else:
                        print("Unknown command, please retry\n")
        print("End of initialization step")

    def run_simulation(self) -> None:
        """
        Run simulation of life in a paddock

        Returns
        -------
        None
        """
        print("Let's start simulation step")
        continue_simulation = True
        while continue_simulation:
            print("Enter number of day(s) you want to simulate (positiv integer) or q in order to quit")
            answer = input()
            if answer.lower() == 'q':
                continue_simulation = False
            else:
                try:
                    nb_day_to_simulate = int(answer)
                    if nb_day_to_simulate > 0 and nb_day_to_simulate < 1095:
                        # It's probably a good idea to prevent a too long simulation (> 3 years)
                        for d in range(nb_day_to_simulate):
                            self.and_one_more_day()

                except ValueError:
                    print(f"{answer} is not a valid integer")
        print("End of simulation step")

    def add_plant(self, plant: Plant) -> None:
        """
        Add the plant to the paddock

        Parameters
        ----------
        plant : Plant
            Plant to add in the paddock

        Returns
        -------
        None
        """
        self.lst_living_entity.append(plant)

    def add_animal(self, animal: Animal) -> None:
        """
        Add the animal to the paddock

        Parameters
        ----------
        animal : Animal
            Animal to add in the paddock

        Returns
        -------
        None
        """
        self.lst_living_entity.append(animal)

    def and_one_more_day(self) -> None:
        """
        Do day's action(s) and display a report

        Returns
        -------
        None
        """
        # No action for the moment

        # Then display the report
        print(self.create_report())

    def create_report(self) -> str:
        """
        Create a report for the paddock

        Returns
        -------
        A string containing the report
        """
        ret = (f"Number of plant(s) {len( [le for le in self.lst_living_entity if isinstance(le, Plant) ])}\n")

        ret += "Animal(s):\n"
        for animal in [le for le in self.lst_living_entity if isinstance(le, Animal)]:
            ret += f"\t{animal}\n"

        ret += "---------------\n"
        return ret
