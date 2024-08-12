from typing import Protocol, Dict
import uuid

UniqueIdentifier = str | uuid.UUID | int

class IdentifiableProtocol(Protocol):
    def id(self) -> UniqueIdentifier:
        pass

class ComparableProtocol(Protocol):
    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ne__(self, other):
        pass

class DictableProtocol(Protocol):
    def to_dict(self) -> Dict:
        raise NotImplementedError()


class JsonableProtocol(DictableProtocol):
    def to_json(self) -> str:
        raise NotImplementedError()
