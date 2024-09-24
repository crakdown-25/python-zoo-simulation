from zoo_simulation.living_entity import LivingEntity, STANDARD_AGE_FOR_TEST
import zoo_simulation.paddock as simuation_paddock
import os


class TestZooSimulation:

    # Setup method (will be called before running tests)
    def setup_class(cls):
        LivingEntity.testing_mode = True

    # Teaddown methode (will be called at tests end)
    def teardown_class(cls):
        LivingEntity.testing_mode = False

    # Test Paddock initialization (whith blank input)
    def test_empty_initialization(self):
        input_values = ['q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Plant(s)\n0❤️\n0💀\nAnimal(s):\n---------------\n"""

    # Test Paddock initialization (whith one plant)
    def test_one_plant_initialization(self):
        input_values = ['Plant', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        print(report)
        assert report == """Plant(s)\n1❤️\n0💀\nAnimal(s):\n---------------\n"""

    # Test Paddock initialization (whith several plants)
    def test_five_plant_initialization(self):
        input_values = ['Plant 5', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Plant(s)\n5❤️\n0💀\nAnimal(s):\n---------------\n"""

    # Test Paddock initialization (whith one plant and one lion)
    def test_one_plant_and_one_lion_initialization(self):
        input_values = ['Plant', 'Lion lion1 m', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == f"""Plant(s)\n1❤️\n0💀\nAnimal(s):\n\t🦁 Lion lion1 ♂️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n---------------\n"""

    # Test Paddock initialization (whith four plants, one tiger and one elephant)
    def test_four_plants_one_tiger_one_elephant_initialization(self):
        input_values = ['Plant 4', 'Tiger woods m', 'Elephant Céleste f', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == f"""Plant(s)\n4❤️\n0💀\nAnimal(s):\n\t🐅 Tiger woods ♂️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n\t🐘 Elephant Céleste ♀️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n---------------\n"""

    # Test Paddock initialization (whith four plants, one tiger and one elephant)
    def test_one_plant_and_one_coyote_one_giraffe_initialization(self):
        input_values = ['Plant', 'Coyote vil_coyote m', 'Giraffe Sophie f', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == f"""Plant(s)\n1❤️\n0💀\nAnimal(s):\n\t🦊 Coyote vil_coyote ♂️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n\t🦒 Giraffe Sophie ♀️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n---------------\n"""

    # Test Paddock initialization (whith two plants, two antelopes)
    def test_two_plants_and_two_antelopes_initialization(self):
        input_values = ['Plant', 'Plant', 'Antelope Jean m', 'Antelope Marie f', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == f"""Plant(s)\n2❤️\n0💀\nAnimal(s):\n\t𓃴 Antelope Jean ♂️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n\t𓃴 Antelope Marie ♀️ PV 10 Age {STANDARD_AGE_FOR_TEST} ❤️\n---------------\n"""

    # Test saving configuration
    def test_saving_configuration(self):
        reference_file = os.path.join('tests', 'Beauval.json')
        current_json_file = 'test_saving.json'

        input_values = ['Plant', 'Plant', 'Lion lion1 m', 'Tiger woods m', 'Elephant Céleste f', 's', current_json_file, 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()

        f = open(reference_file, "r").read()
        f2 = open(current_json_file, "r").read()

        test_result = f == f2

        try:
            os.remove(current_json_file)
        except OSError:
            pass

        assert test_result, f"File {f} and {f2} are differents"

    # Test loading configuration
    def test_loading_configuration(self):
        reference_file = os.path.join('tests', 'Beauval.json')

        input_values = ['l', reference_file, 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()

        res = paddock.create_report()

        assert res == """Plant(s)\n2❤️\n0💀\nAnimal(s):\n	🦁 Lion lion1 ♂️ PV 10 Age 12 ❤️\n	🐅 Tiger woods ♂️ PV 10 Age 12 ❤️\n	🐘 Elephant Céleste ♀️ PV 10 Age 12 ❤️\n---------------\n""", "Paddock content is not correct"

    # Test saving/loading complete simulation to binary file
    def test_saving_loading_binary(self):
        current_binary_file = 'test_saving.binary'
        empty_binary_file = os.path.join('tests', 'empty.binary')

        input_values = ['Plant', 'Plant', 'Lion lion1 m', 'Tiger woods m', 'Elephant Céleste f', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()

        input_values = ['1', 's', current_binary_file, 'l', empty_binary_file, 'q']
        simuation_paddock.input = mock_input
        paddock.run_simulation()

        assert paddock.paddock_age == 0, "Paddock age should be 0"
        assert len(paddock.lst_living_entity) == 0, "Paddock len(lst_living_entity) should be 0"

    # Test loading complete simulation to binary file
    def test_loading_binary(self):
        current_binary_file = 'test_saving.binary'
        assert os.path.isfile(current_binary_file), f"File {current_binary_file} is missing"

        input_values = ['lsimulation', current_binary_file, 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()

        assert paddock.paddock_age == 1, "Paddock age should be 1"
        assert len(paddock.lst_living_entity) == 7, "Paddock len(lst_living_entity) should be 7"
