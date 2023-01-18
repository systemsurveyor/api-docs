custom_texts = {
  '<h1 id="system-surveyor-api-folders">Folders</h1>': '<h3>Test</h3>',
}

# Read in the file
file_path = "source/index.html.md"
with open(file_path, 'r') as file :
  filedata = file.read()

# Replace the target string
for key, value in custom_texts.items():
  filedata = filedata.replace(key, key+value)

# Write the file out again
with open(file_path, 'w') as file:
  file.write(filedata)
