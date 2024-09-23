from zoo_simulation.living_entity import LivingEntity, Plant, Animal, Sex
from zoo_simulation.living_entity import Carnivorous, Herbivore
from zoo_simulation.living_entity import Lion, Tiger, Coyote, Elephant, Giraffe, Antelope


class TestLivingEntity:

    # Test if LivingEntity is an abstract class
    def test_livingentity_instantiation_forbidden(self):
        try:
            _ = LivingEntity()
            assert False, "abstract class LivingEntity musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class LivingEntity with abstract method __repr__"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_animal_instantiation_forbidden(self):
        try:
            _ = Animal()
            assert False, "abstract class Animal musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Animal with abstract methods can_eat, eat"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_carnivorous_instantiation_forbidden(self):
        try:
            _ = Carnivorous()
            assert False, "abstract class Carnivorous musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Carnivorous with abstract method eat"
        except Exception:
            assert False, "wrong exception type (need to be TypeError)"

    # Test if Animal is an abstract class
    def test_herbivore_instantiation_forbidden(self):
        try:
            _ = Herbivore()
            assert False, "abstract class Herbivore musn't be instantiable"
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Herbivore with abstract method eat"
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
        assert str(lion1) == '🦁 Lion lion1 ♂️'

        try:
            lion2 = Lion("lion2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Lion instantiation"
        assert str(lion2) == '🦁 Lion lion2 ♀️'

    # Test we can create an object of Tiger class (check representation too)
    def test_tiger_instantiation_representation(self):
        try:
            tiger1 = Tiger("woods", Sex.MALE)
        except Exception:
            assert False, "Exception during Tiger instantiation"
        assert str(tiger1) == '🐅 Tiger woods ♂️'

        try:
            tiger2 = Tiger("tiger2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Tiger instantiation"
        assert str(tiger2) == '🐅 Tiger tiger2 ♀️'

    # Test we can create an object of Coyote class (check representation too)
    def test_coyote_instantiation_representation(self):
        try:
            coyote1 = Coyote("coyote1", Sex.MALE)
        except Exception:
            assert False, "Exception during Coyote instantiation"
        assert str(coyote1) == '🦊 Coyote coyote1 ♂️'

        try:
            coyote2 = Coyote("coyote2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Coyote instantiation"
        assert str(coyote2) == '🦊 Coyote coyote2 ♀️'

    # Test we can create an object of Elephant class (check representation too)
    def test_elephant_instantiation_representation(self):
        try:
            elephant1 = Elephant("elephant1", Sex.MALE)
        except Exception:
            assert False, "Exception during Elephant instantiation"
        assert str(elephant1) == '🐘 Elephant elephant1 ♂️'

        try:
            elephant2 = Elephant("elephant2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Elephant instantiation"
        assert str(elephant2) == '🐘 Elephant elephant2 ♀️'

    # Test we can create an object of Giraffe class (check representation too)
    def test_giraffe_instantiation_representation(self):
        try:
            giraffe1 = Giraffe("giraffe1", Sex.MALE)
        except Exception:
            assert False, "Exception during Giraffe instantiation"
        assert str(giraffe1) == '🦒 Giraffe giraffe1 ♂️'

        try:
            giraffe2 = Giraffe("giraffe2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Giraffe instantiation"
        assert str(giraffe2) == '🦒 Giraffe giraffe2 ♀️'

    # Test we can create an object of Antelope class (check representation too)
    def test_antelope_instantiation_representation(self):
        try:
            antelope1 = Antelope("antelope1", Sex.MALE)
        except Exception:
            assert False, "Exception during Antelope instantiation"
        assert str(antelope1) == '𓃴 Antelope antelope1 ♂️'

        try:
            antelope2 = Antelope("antelope2", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Antelope instantiation"
        assert str(antelope2) == '𓃴 Antelope antelope2 ♀️'
