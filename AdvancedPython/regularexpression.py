# Extract a 10-digit phone number from text. 

import re

text = "My phone number is 9860000000. Call me ."

pattern = r"\b\d{10}\b"
result = re.findall(pattern, text)

print(result)
