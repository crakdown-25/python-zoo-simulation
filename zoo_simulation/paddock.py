import re
import json
from typing import Dict
from io import StringIO
from .living_entity import LivingEntity, Plant, Sex, Animal, Lion, Tiger, Coyote, Elephant, Giraffe, Antelope


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
    remove_all_plants_and_all_animals()
        Remove all plants and animals in the paddock

    initialization()
        Allow user to make initialization of the paddock

    run_simulation()
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

    def remove_all_plants_and_all_animals(self) -> None:
        """
        Remove all plants and animals in the paddock
        """
        self.lst_living_entity.clear()

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
        lst_new_entities: list[LivingEntity] = []
        # Since story #3, we have to manage actions in the paddock
        for living_entity in self.lst_living_entity:
            new_entity = living_entity.do_actions(self.lst_living_entity)
            if new_entity:
                lst_new_entities.append(new_entity)

        # In a second time, we add new_entity
        for entity in lst_new_entities:
            if isinstance(entity, Animal):
                self.add_animal(entity)
            elif isinstance(entity, Plant):
                self.add_plant(entity)

        # Then display the report
        print(self.create_report())

    def create_report(self) -> str:
        """
        Create a report for the paddock

        Returns
        -------
        A string containing the report
        """

        alive_plants = [le for le in self.lst_living_entity if isinstance(le, Plant) and le.is_alive]
        dead_plants = [le for le in self.lst_living_entity if isinstance(le, Plant) and not le.is_alive]
        ret = (f"Plant(s)\n{len(alive_plants)}❤️\n{len(dead_plants)}💀\n")

        ret += "Animal(s):\n"
        for animal in [le for le in self.lst_living_entity if isinstance(le, Animal)]:
            ret += f"\t{animal}\n"

        ret += "---------------\n"
        return ret

    def initialization(self) -> None:
        """
        Allow user to make initialization of the paddock

        Returns
        -------
        None
        """
        print("Let's start initialization step")
        animals_dict: Dict = {f"{e.__name__}": e for e in [Lion, Tiger, Coyote, Elephant, Giraffe, Antelope]}
        pattern = r'^[Pp][Ll][Aa][Nn][Tt] (\d+)$'
        continue_initialization = True
        while continue_initialization:
            print("Enter 'Plant' to add a plant")
            print("Enter 'Plant X (X : a positive integer)' to add X plants")
            print("Enter 'Lion/Tiger/Coyote/Elephant/Giraffe/Antelope animal_name m/f' to add an animal")
            print("Enter 's' to store current configuration to JSON file")
            print("Enter 'l' to load a JSON file as current configuration( WARNING existing living entity will be ereased)")
            print("Enter 'v' to view paddock content")
            print("Enter 'q' to stop initilization step")
            answer = input()
            match answer.lower():
                case "q":
                    continue_initialization = False
                case "plant":
                    self.add_plant(Plant())
                    print("One plant added\n")
                case 'v':
                    print(self.create_report())
                case 's':
                    print("Enter JSON filename (it will be store in the current directory)")
                    filename = input()
                    try:
                        with open(filename, 'w') as fpjson:
                            for le in self.lst_living_entity:
                                dict_to_serialize = dict(le.__dict__)
                                dict_to_serialize['__name__'] = le.__class__.__name__
                                le_json_dict = json.dumps(dict_to_serialize, default=str)
                                fpjson.write(f"{le_json_dict}\n")
                            print(f"JSON file {filename} written")
                    except Exception as e:
                        print(f'{e} during JSON file "{filename}" writting')
                case 'l':
                    print("Enter JSON filename (it will be store in the current directory)")
                    filename = input()
                    try:
                        with open(filename, 'r') as fpjson:
                            self.remove_all_plants_and_all_animals()
                            lines = fpjson.readlines()
                            for line in lines:
                                io = StringIO(line)
                                le_dict = json.load(io)
                                if le_dict['__name__'] == 'Plant':
                                    plant = Plant(age=le_dict['_age'])
                                    for k, v in le_dict.items():
                                        if k not in ['__name__', '_age']:
                                            plant.__dict__[k] = v
                                    self.add_plant(plant)
                                else:
                                    entity = animals_dict[le_dict['__name__']](le_dict['name'], Sex.MALE if le_dict['sex'] == 'Sex.MALE' else Sex.FEMALE, age=le_dict['_age'])
                                    for k, v in le_dict.items():
                                        if k not in ['__name__', 'name', 'sex', '_age']:
                                            entity.__dict__[k] = v
                                    self.add_animal(entity)
                    except Exception as e:
                        print(f'{e} during JSON file "{filename}" loading')
                case _:
                    if len(infos := answer.split(" ")) == 3 and \
                            infos[0] in animals_dict and \
                            infos[2].lower() in ['m', 'f']:
                        animal = animals_dict[infos[0]](infos[1], Sex.MALE if infos[2].lower() == 'm' else Sex.FEMALE)
                        self.add_animal(animal)
                        print(f"{animal}  added\n")
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
                    if nb_day_to_simulate <= 0:
                        print("Number of day(s) needs to be a positiv integer")
                    elif nb_day_to_simulate > 1095:
                        print("Number of day(s) needs to be a less than 1095 (3 years)")
                    else:
                        # It's probably a good idea to prevent a too long simulation (> 3 years)
                        for d in range(nb_day_to_simulate):
                            self.and_one_more_day()

                except ValueError:
                    print(f"{answer} is not a valid integer")
        print("End of simulation step")
