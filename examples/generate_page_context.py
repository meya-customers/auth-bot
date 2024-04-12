import time

from component.sha256 import compute_hmac_sha256_signature

# example
ttl = 30  # 30 seconds
current_timestamp = int(time.time()) + ttl
user_id = "erik@meya.ai"
secret = "solar_eclipse"
computed_signature = compute_hmac_sha256_signature(
    f"{user_id}{current_timestamp}", secret
)
print(computed_signature)
print(
    f"""
            pageContext: {{
                expires: {current_timestamp},
                user_hash: "{computed_signature}"
            }}
"""
)

# confirm with https://www.freeformatter.com/hmac-generator.html#before-output
# assert computed_signature == "fbafc1e2deedcf00932e64f8112b82774b6c4fa1430ee2543337b1d6da135e19"
