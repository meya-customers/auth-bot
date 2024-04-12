import hashlib
import hmac

from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


def compute_hmac_sha256_signature(string, secret):
    hashed = hmac.new(
        secret.encode("utf-8"), string.encode("utf-8"), hashlib.sha256
    )
    return hashed.digest().hex()


@dataclass
class Sha256ComponentElement(Component):
    string: str = element_field()
    secret: str = element_field()

    async def start(self) -> List[Entry]:
        computed_signature = compute_hmac_sha256_signature(
            self.string, self.secret
        )
        return self.respond(data=dict(result=computed_signature))
