from zoo_simulation.living_entity import LivingEntity, Plant, Animal, Sex


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

    # Test we can create an object of Plant class
    def test_plant_instantiation(self):
        try:
            _ = Plant()
        except Exception:
            assert False, "Exception during Plant instantiation"

    # Test we can create an object of Animal class
    def test_animal_instantiation(self):
        try:
            _ = Animal("Babar", Sex.MALE)
        except Exception:
            assert False, "Exception during Animal instantiation"

        try:
            _ = Animal("Céleste", Sex.FEMALE)
        except Exception:
            assert False, "Exception during Animal instantiation"

    def test_animal_representation(self):
        babar = Animal("Babar", Sex.MALE)
        assert str(babar) == 'Animal Babar ♂️'

        celeste = Animal("Céleste", Sex.FEMALE)
        assert str(celeste) == 'Animal Céleste ♀️'
