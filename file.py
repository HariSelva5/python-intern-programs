import os
os.remove("hi.")
if os.path.exists("hi"):
  os.remove("hi")
else:
  print("The file does not exist")
