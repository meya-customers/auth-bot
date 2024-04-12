import pytest

from component.sha256 import compute_hmac_sha256_signature

# check online with https://devglan.com/online-tools/hmac-sha256-online


@pytest.mark.parametrize(
    ("string", "secret", "computed_hash"),
    [
        (
            "erik@meya.ai",
            "solar_eclipse",
            "c99b34b1bf5f83f61f3d77f0bae4633a49ee857061634e0e67668edd45944911",
        ),
        (
            "erik@meya.ai1712881476",
            "solar_eclipse",
            "031d822ebc78950a475b0ba8f117b0aae44c6df5a7045e993324b9c46ae94a88",
        ),
    ],
)
def test_square(string: str, secret: str, computed_hash: str):
    assert compute_hmac_sha256_signature(string, secret) == computed_hash
