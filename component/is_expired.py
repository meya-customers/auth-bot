import time

from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


def is_timestamp_expired(timestamp):
    current_timestamp = int(time.time())
    return timestamp < current_timestamp


@dataclass
class IsExpiredComponentElement(Component):
    timestamp: int = element_field()

    async def start(self) -> List[Entry]:
        return self.respond(
            data=dict(result=is_timestamp_expired(self.timestamp))
        )
