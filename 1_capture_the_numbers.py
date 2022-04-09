import re

pattern = r"\d+"

nums = [0]

while True:
    text = input()
    if not text:
        break

    result = re.findall(pattern, text)
    if len(result) > 0:

        print(" ".join(result), end=" ")




