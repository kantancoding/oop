from abc import ABC, abstractmethod
import platform


class Accessory(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class BlueLightSaber(Accessory):
    def render(self) -> str:
        return "render BLUE lightsaber"


class RedLightSaber(Accessory):
    def render(self) -> str:
        return "render RED lightsaber"


class RedEyes(Accessory):
    def render(self) -> str:
        return "render RED eyes"


class BlueEyes(Accessory):
    def render(self) -> str:
        return "render BLUE eyes"


class BlackRobe(Accessory):
    def render(self) -> str:
        return "render BLACK robe"


class WhiteRobe(Accessory):
    def render(self) -> str:
        return "render WHITE robe"


class AbstractAccessoryFactory():
    @abstractmethod
    def create_light_saber(self) -> Accessory:
        pass

    @abstractmethod
    def create_eyes(self) -> Accessory:
        pass

    @abstractmethod
    def create_robe(self) -> Accessory:
        pass


class SithAccessoryFactory(AbstractAccessoryFactory):
    # def create_light_saber(self) -> Accessory:
    #     return RedLightSaber()

    def create_eyes(self) -> Accessory:
        return RedEyes()

    def create_robe(self) -> Accessory:
        return BlackRobe()


class JediAccessoryFactory(AbstractAccessoryFactory):
    def create_light_saber(self) -> Accessory:
        return BlueLightSaber()

    def create_eyes(self) -> Accessory:
        return BlueEyes()

    def create_robe(self) -> Accessory:
        return WhiteRobe()


def client(accessory_factory: AbstractAccessoryFactory) -> None:
    lightsaber = accessory_factory.create_light_saber()
    robe = accessory_factory.create_robe()
    eyes = accessory_factory.create_eyes()

    print(eyes.render())
    print(lightsaber.render())
    print(robe.render())


if __name__ == "__main__":
    current_os = platform.system()

    if current_os == "Windows":
        client(JediAccessoryFactory())
    elif current_os == "Darwin":
        client(SithAccessoryFactory())
    else:
        print("OS not supported!")
