from dataclasses import dataclass
from ..payload import DataPayload
from ..utility.common_models import Name

@dataclass(frozen=True)
class EncounterMethod:

    data : DataPayload

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def order(self):
        return self.data.get("order")

    @property
    def names(self):
        return [Name(_) for _ in self.data.get("names")]