from abc import ABC, abstractmethod


# Abstract Product: Asteroids
class Asteroid(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


# Concrete Products

class GoldAsteroid(Asteroid):
    def show(self) -> None:
        print("Gold Asteroid popped up")


class SiliconAsteroid(Asteroid):
    def show(self) -> None:
        print("Silicon Asteroid popped up")


class CrystalAsteroid(Asteroid):
    def show(self) -> None:
        print("Crystal Asteroid popped up")


class DiamondAsteroid(Asteroid):
    def show(self) -> None:
        print("Diamond Asteroid popped up")


class IceAsteroid(Asteroid):
    def show(self) -> None:
        print("Ice Asteroid popped up")


class IronAsteroid(Asteroid):
    def show(self) -> None:
        print("Iron Asteroid popped up")


class RockyAsteroid(Asteroid):
    def show(self) -> None:
        print("Rocky Asteroid popped up")


class DebrisField(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


class RockDebrisField(DebrisField):
    def show(self) -> None:
        print("A rock debris field has appeared!")


class ToxicDebrisField(DebrisField):
    def show(self) -> None:
        print("A toxic debris field has appeared!")


class MagneticDebrisField(DebrisField):
    def show(self) -> None:
        print("A magnetic debris field has appeared!")


class ExplosiveDebrisField(DebrisField):
    def show(self) -> None:
        print("An explosive debris field has appeared!")


class PersistentDebrisField(DebrisField):
    def show(self) -> None:
        print("A persistent debris field has appeared!")


class DynamicDebrisField(DebrisField):
    def show(self) -> None:
        print("A dynamic debris field has appeared!")


class ObstacleFactory(ABC):
    @abstractmethod
    def create_asteroid(self) -> Asteroid:
        pass

    @abstractmethod
    def create_debris_field(self) -> DebrisField:
        pass


# Concrete Factories: Level1Factory, Level2Factory, Level3Factory, Level4Factory, Level5Factory
class Level1Factory(ObstacleFactory):
    def create_asteroid(self) -> Asteroid:
        return RockyAsteroid()

    def create_debris_field(self) -> DebrisField:
        return RockDebrisField()


class Level2Factory(ObstacleFactory):
    def create_asteroid(self) -> Asteroid:
        return IronAsteroid()

    def create_debris_field(self) -> DebrisField:
        return ToxicDebrisField()


class Level3Factory(ObstacleFactory):
    def create_asteroid(self) -> Asteroid:
        return DiamondAsteroid()

    def create_debris_field(self) -> DebrisField:
        return ExplosiveDebrisField()


class Level4Factory(ObstacleFactory):
    def create_asteroid(self) -> Asteroid:
        return GoldAsteroid()

    def create_debris_field(self) -> DebrisField:
        return MagneticDebrisField()


class Level5Factory(ObstacleFactory):
    def create_asteroid(self) -> Asteroid:
        return CrystalAsteroid()

    def create_debris_field(self) -> DebrisField:
        return PersistentDebrisField()


# Client
def main() -> None:
    import random

    # Randomly select a level
    level = random.choice([1, 2, 3, 4, 5])

    # Get the appropriate factory
    factory = get_factory(level)

    # Create an asteroid using the factory
    asteroid = factory.create_asteroid()
    asteroid.show()

    # Create a debris field using the factory
    debris_field = factory.create_debris_field()
    debris_field.show()


def get_factory(level: int) -> ObstacleFactory:
    return {
        1: Level1Factory(),
        2: Level2Factory(),
        3: Level3Factory(),
        4: Level4Factory(),
        5: Level5Factory(),
    }[level]


if __name__ == "__main__":
    main()
