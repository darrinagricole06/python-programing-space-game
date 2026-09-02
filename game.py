from engine.display import show_intro
from engine.galaxy import create_galaxy
from engine.journey import travel
import constants

def should_stop_fn() -> bool:
    answer = input("Do you want to continue your journey? (y/n): ")

    if answer == "y":
        return True
    else:
        return False

def main():
    show_intro(constants.SHIP_NAME, constants.CREW_DESCRIPTION)
    galaxy = create_galaxy(constants.GALAXY_SIZE)
    travel(
        galaxy,
        constants.STARTING_OXYGEN,
        constants.STARTING_HULL,
        constants.SHIP_NAME,
        should_stop_fn
    )


if __name__ == "__main__":
    main()
