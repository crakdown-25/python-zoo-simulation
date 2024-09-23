from zoo_simulation.paddock import Paddock

if __name__ == "__main__":
    print("Welcome to Zoo simulation")

    # Create the new paddock
    paddock = Paddock()
    # And initialize it
    paddock.initialization()
    # Then launch the simulation
    paddock.run_simulation()

    print("Bye")
