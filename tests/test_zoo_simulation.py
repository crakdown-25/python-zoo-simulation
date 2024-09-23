import zoo_simulation.paddock as simuation_paddock


class TestZooSimulation:

    # Test Paddock initialization (whith blank input)
    def test_empty_initialization(self):
        input_values = ['q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Number of plant(s) 0\nAnimal(s):\n---------------\n"""

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
        assert report == """Number of plant(s) 1\nAnimal(s):\n---------------\n"""

    # Test Paddock initialization (whith several plants)
    def test_five_plant_initialization(self):
        input_values = ['Plant 5', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Number of plant(s) 5\nAnimal(s):\n---------------\n"""

    # Test Paddock initialization (whith one plant and one animal)
    def test_one_plant_and_one_animal_initialization(self):
        input_values = ['Plant', 'Animal Babar m', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Number of plant(s) 1\nAnimal(s):\n\tAnimal Babar ♂️\n---------------\n"""

    # Test Paddock initialization (whith four plants and two animals)
    def test_one_plant_and_two_animals_initialization(self):
        input_values = ['Plant 4', 'Animal Babar m', 'Animal Céleste f', 'q']

        def mock_input(s=None):
            return input_values.pop(0)

        simuation_paddock.input = mock_input
        paddock = simuation_paddock.Paddock()
        paddock.initialization()
        report = paddock.create_report()
        assert report == """Number of plant(s) 4\nAnimal(s):\n\tAnimal Babar ♂️\n\tAnimal Céleste ♀️\n---------------\n"""
