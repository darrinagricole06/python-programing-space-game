from engine.display import show_intro
from engine.galaxy import create_galaxy
from engine.journey import travel
import constants


def main():
    show_intro(constants.SHIP_NAME, constants.CREW_DESCRIPTION)
    galaxy = create_galaxy(constants.GALAXY_SIZE)
    travel(
        galaxy,
        constants.STARTING_OXYGEN,
        constants.STARTING_HULL,
        constants.SHIP_NAME,
    )


if __name__ == "__main__":
    main()
