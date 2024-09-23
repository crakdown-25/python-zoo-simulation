from zoo_simulation.living_entity import LivingEntity, Plant, Animal, Sex
from zoo_simulation.living_entity import Carnivorous, Herbivore
from zoo_simulation.living_entity import Lion, Tiger, Coyote, Elephant, Giraffe, Antelope
from zoo_simulation.living_entity import PV_LOSTS_ANIMAL_WHEN_EATEN, PV_OBTAINED_CARNIVOROUS_BY_ANIMAL
from zoo_simulation.living_entity import PV_LOSTS_PLANT_WHEN_EATEN, PV_OBTAINED_HERBIVORE_BY_PLANT


class TestLivingEntity:

    # Test if LivingEntity is an abstract class
    def test_livingentity_instantiation_forbidden(self):
        try:
            _ = LivingEntity()
            assert False, "abstract class LivingEntity musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class LivingEntity with abstract methods __repr__, do_actions, gets_eaten"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_animal_instantiation_forbidden(self):
        try:
            _ = Animal()
            assert False, "abstract class Animal musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Animal with abstract method can_eat"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_carnivorous_instantiation_forbidden(self):
        try:
            _ = Carnivorous()
            assert False, "abstract class Carnivorous musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Carnivorous with abstract method can_eat"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_herbivore_instantiation_forbidden(self):
        try:
            _ = Herbivore()
            assert False, "abstract class Herbivore musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Herbivore with abstract method can_eat"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test we can create an object of Plant class
    def test_plant_instantiation(self):
        try:
            _ = Plant()
        except Exception:
            assert False, "Exception during Plant instantiation"

    # Test we can create an object of Lion class (check representation too)
    def test_lion_instantiation_representation(self):
        try:
            lion1 = Lion("lion1", Sex.MALE)
        except Exception:
            assert False, "Exception during Lion instantiation"
        assert str(lion1) == '🦁 Lion lion1 ♂️ PV 10 ❤️'

        try:
            lion2 = Lion("lion2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Lion instantiation"
        assert str(lion2) == '🦁 Lion lion2 ♀️ PV 10 ❤️'

    # Test we can create an object of Tiger class (check representation too)
    def test_tiger_instantiation_representation(self):
        try:
            tiger1 = Tiger("woods", Sex.MALE)
        except Exception:
            assert False, "Exception during Tiger instantiation"
        assert str(tiger1) == '🐅 Tiger woods ♂️ PV 10 ❤️'

        try:
            tiger2 = Tiger("tiger2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Tiger instantiation"
        assert str(tiger2) == '🐅 Tiger tiger2 ♀️ PV 10 ❤️'

    # Test we can create an object of Coyote class (check representation too)
    def test_coyote_instantiation_representation(self):
        try:
            coyote1 = Coyote("coyote1", Sex.MALE)
        except Exception:
            assert False, "Exception during Coyote instantiation"
        assert str(coyote1) == '🦊 Coyote coyote1 ♂️ PV 10 ❤️'

        try:
            coyote2 = Coyote("coyote2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Coyote instantiation"
        assert str(coyote2) == '🦊 Coyote coyote2 ♀️ PV 10 ❤️'

    # Test we can create an object of Elephant class (check representation too)
    def test_elephant_instantiation_representation(self):
        try:
            elephant1 = Elephant("elephant1", Sex.MALE)
        except Exception:
            assert False, "Exception during Elephant instantiation"
        assert str(elephant1) == '🐘 Elephant elephant1 ♂️ PV 10 ❤️'

        try:
            elephant2 = Elephant("elephant2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Elephant instantiation"
        assert str(elephant2) == '🐘 Elephant elephant2 ♀️ PV 10 ❤️'

    # Test we can create an object of Giraffe class (check representation too)
    def test_giraffe_instantiation_representation(self):
        try:
            giraffe1 = Giraffe("giraffe1", Sex.MALE)
        except Exception:
            assert False, "Exception during Giraffe instantiation"
        assert str(giraffe1) == '🦒 Giraffe giraffe1 ♂️ PV 10 ❤️'

        try:
            giraffe2 = Giraffe("giraffe2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Giraffe instantiation"
        assert str(giraffe2) == '🦒 Giraffe giraffe2 ♀️ PV 10 ❤️'

    # Test we can create an object of Antelope class (check representation too)
    def test_antelope_instantiation_representation(self):
        try:
            antelope1 = Antelope("antelope1", Sex.MALE)
        except Exception:
            assert False, "Exception during Antelope instantiation"
        assert str(antelope1) == '𓃴 Antelope antelope1 ♂️ PV 10 ❤️'

        try:
            antelope2 = Antelope("antelope2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Antelope instantiation"
        assert str(antelope2) == '𓃴 Antelope antelope2 ♀️ PV 10 ❤️'

    # Test an animal cannot eat himself
    def test_animal_non_autophagy(self):
        antelope1 = Antelope("antelope1", Sex.MALE)
        giraffe1 = Giraffe("giraffe1", Sex.MALE)
        elephant1 = Elephant("elephant1", Sex.MALE)
        coyote1 = Coyote("coyote1", Sex.MALE)
        tiger1 = Tiger("woods", Sex.MALE)
        lion1 = Lion("lion1", Sex.MALE)

        assert not antelope1.can_eat(antelope1), "Antelope musn't eat himself"
        assert not giraffe1.can_eat(giraffe1), "Giraffe musn't eat himself"
        assert not elephant1.can_eat(elephant1), "Elephant musn't eat himself"
        assert not coyote1.can_eat(coyote1), "Coyote musn't eat himself"
        assert not tiger1.can_eat(tiger1), "Tiger musn't eat himself"
        assert not lion1.can_eat(lion1), "Lion musn't eat himself"

    # Test an animal cannot eat another animal with the same species
    def test_animal_cannot_eat_same_species(self):
        antelope1 = Antelope("antelope1", Sex.MALE)
        antelope2 = Antelope("antelope2", Sex.MALE)
        giraffe1 = Giraffe("giraffe1", Sex.MALE)
        giraffe2 = Giraffe("giraffe2", Sex.MALE)
        elephant1 = Elephant("elephant1", Sex.MALE)
        elephant2 = Elephant("elephant1", Sex.MALE)
        coyote1 = Coyote("coyote1", Sex.MALE)
        coyote2 = Coyote("coyote2", Sex.MALE)
        tiger1 = Tiger("woods", Sex.MALE)
        tiger2 = Tiger("woods2", Sex.MALE)
        lion1 = Lion("lion1", Sex.MALE)
        lion2 = Lion("lion2", Sex.MALE)

        assert not antelope1.can_eat(antelope2), "Antelope musn't eat another Antelope"
        assert not giraffe1.can_eat(giraffe2), "Giraffe musn't eat another Giraffe"
        assert not elephant1.can_eat(elephant2), "Elephant musn't eat another Elephant"
        assert not coyote1.can_eat(coyote2), "Coyote musn't eat another Coyote"
        assert not tiger1.can_eat(tiger2), "Tiger musn't eat another Tiger"
        assert not lion1.can_eat(lion2), "Lion musn't eat another Lion"

    # Test an animal cannot eat dead animal / plant
    def test_animal_cannot_eat_dead_entity(self):
        antelope1 = Antelope("antelope1", Sex.MALE)
        antelope2 = Antelope("antelope2", Sex.MALE)
        antelope2._is_alive = False
        giraffe1 = Giraffe("giraffe1", Sex.MALE)
        giraffe2 = Giraffe("giraffe2", Sex.MALE)
        giraffe2._is_alive = False
        elephant1 = Elephant("elephant1", Sex.MALE)
        elephant2 = Elephant("elephant1", Sex.MALE)
        elephant2._is_alive = False
        coyote1 = Coyote("coyote1", Sex.MALE)
        coyote2 = Coyote("coyote2", Sex.MALE)
        coyote2._is_alive = False
        tiger1 = Tiger("woods", Sex.MALE)
        tiger2 = Tiger("woods2", Sex.MALE)
        tiger2._is_alive = False
        lion1 = Lion("lion1", Sex.MALE)
        lion2 = Lion("lion2", Sex.MALE)
        lion2._is_alive = False
        plant = Plant()
        plant._is_alive = False

        assert not antelope1.can_eat(plant), "Antelope musn't eat dead Plant"
        assert not giraffe1.can_eat(plant), "Giraffe musn't eat dead Plant"
        assert not elephant1.can_eat(plant), "Elephant musn't eat dead Plant"
        assert not coyote1.can_eat(antelope2), "Coyote musn't eat dead Antelope"
        assert not tiger1.can_eat(lion2), "Tiger musn't eat dead Lion"
        assert not lion1.can_eat(elephant2), "Lion musn't eat dead Elephant"

    # Test PV evolution during eating
    def test_pv_evolution_during_eating(self):
        antelope1 = Antelope("antelope1", Sex.MALE)
        antelope2 = Antelope("antelope2", Sex.MALE)
        tiger1 = Tiger("woods", Sex.MALE)
        plant = Plant()

        tiger1.eat(antelope1)
        assert tiger1.life_point == 10 + PV_OBTAINED_CARNIVOROUS_BY_ANIMAL, f"Tiger PV must be {10 + PV_OBTAINED_CARNIVOROUS_BY_ANIMAL}"
        assert antelope1.life_point == 10 - PV_LOSTS_ANIMAL_WHEN_EATEN, f"Antelope PV must be {10 - PV_LOSTS_ANIMAL_WHEN_EATEN}"

        antelope2.eat(plant)
        assert antelope2.life_point == 10 + PV_OBTAINED_HERBIVORE_BY_PLANT, f"Antelope PV must be {10 + PV_OBTAINED_HERBIVORE_BY_PLANT}"
        assert plant.life_point == 10 - PV_LOSTS_PLANT_WHEN_EATEN, f"Plant PV must be {10 - PV_LOSTS_PLANT_WHEN_EATEN}"
