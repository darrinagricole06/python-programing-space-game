from typing import Literal


class Ship:
    # attributes
    def __init__(
        self,
        oxygen,
        hull,
        name,
        crew
    ) -> None:
        # constructor
        self.oxygen = oxygen
        self.hull = hull
        self.name = name
        self.crew = crew

    # methods
    def __str__(self) -> str:
        return f"""
        Ship object with the following parameters:
        oxygen: {self.oxygen}
        hull: {self.hull}
        name: {self.name}
        crew: {self.crew}
        """

    def check_defeat_status(
        self
    ) -> None | Literal["oxygen depleted", "hull damaged"]:
        if self.oxygen <= 0:
            return "oxygen depleted"
        elif self.hull <= 0:
            return "hull damaged"

        return None


ship_one = Ship(
    10,
    100,
    "The Sr. Explorer",
    "Awesome crew of space explorers"
)

print(ship_one.check_defeat_status())

a = "abc"
print(a.upper())
