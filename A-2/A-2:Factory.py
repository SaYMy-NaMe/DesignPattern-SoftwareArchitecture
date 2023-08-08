import random


class SpaceRock:
    # Abstract product class.

    def show(self) -> None:
        raise NotImplementedError


class IceSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Ice space rocks Detected")


class IronSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Iron space rocks Revealed")


class RockySpaceRock(SpaceRock):

    def show(self) -> None:
        print("Rocky space rocks Emerged")


class SiliconSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Silicon space rocks Arose")


class FireSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Fire space rocks Appeared")


class DiamondSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Diamond space rocks Arrived")


class MagneticSpaceRock(SpaceRock):

    def show(self) -> None:
        print("Magnetic space rocks Materialized")


class SpaceRockFactory:
    # Abstract factory class.

    def create_space_rocks(self, score: int) -> "SpaceRock":
        # Create space rocks based on the score.
        raise NotImplementedError


class Level1SpaceRocksFactory(SpaceRockFactory):

    def create_space_rocks(self, score: int) -> "SpaceRock":
        if score > 200:
            return IceSpaceRock()
        else:
            return IronSpaceRock()


class Level2SpaceRocksFactory(SpaceRockFactory):

    def create_space_rocks(self, score: int) -> "SpaceRock":
        if score > 500:
            return RockySpaceRock()
        else:
            return SiliconSpaceRock()


class Level3SpaceRocksFactory(SpaceRockFactory):

    def create_space_rocks(self, score: int) -> "SpaceRock":
        if score > 1000:
            return FireSpaceRock()
        else:
            return DiamondSpaceRock()


class Level4SpaceRocksFactory(SpaceRockFactory):

    def create_space_rocks(self, score: int) -> "SpaceRock":
        if score > 1500:
            return MagneticSpaceRock()
        else:
            return FireSpaceRock()


def detect_space_rocks() -> None:
    level = random.randint(1, 4)
    score = random.randint(0, 4000)

    # Create the appropriate factory based on the level

    space_rocks_factories = {
        1: Level1SpaceRocksFactory(),
        2: Level2SpaceRocksFactory(),
        3: Level3SpaceRocksFactory(),
        4: Level4SpaceRocksFactory(),
    }

    # Create the appropriate factory based on the level.
    space_rocks_factory = space_rocks_factories[level]

    # Create space rocks based on the score using the factory.
    space_rocks = space_rocks_factory.create_space_rocks(score)

    # Show the type of space rocks that Detected.
    space_rocks.show()

if __name__ == "__main__":
    detect_space_rocks()