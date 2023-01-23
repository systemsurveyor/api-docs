from typing import Dict

# the key is what is currently in the swagger document
# the value is what will be appended after the value
# example: '<h1 id="system-surveyor-api-folders">Folders</h1>': "<h3>Test</h3>"
custom_texts: Dict[str, str] = {}

# Read in the file
file_path = "source/index.html.md"
with open(file_path, "r") as file:
    filedata = file.read()

# Replace the target string
for key, value in custom_texts.items():
    filedata = filedata.replace(key, key + value)

# Write the file out again
with open(file_path, "w") as file:
    file.write(filedata)
