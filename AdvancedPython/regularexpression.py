# Extract a 10-digit phone number from text. 

# para= " Hello I am Shristi. I am doing ont well because the head is paining and I want to do this but still I have to do this only because for the internal which is mine but Mr. Sajjan Acharya is ready to give to me . I am soo frustrated only because of him. "


import re

text = "My phone number is 9860000000. Call me but I am not picking your call understand."

pattern = r"\b\d{10}\b"
result = re.findall(pattern, text)

print(result)
