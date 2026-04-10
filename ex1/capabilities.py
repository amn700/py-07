import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target) -> str:
        raise NotImplementedError


class TransformCapability(abc.ABC):
    STATE = False

    @abc.abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
