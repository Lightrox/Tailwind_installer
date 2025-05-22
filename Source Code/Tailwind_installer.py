import os
import subprocess
import time
import webbrowser
user_name=os.getcwd().split("\\")[2]
body_text="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tailwind CSS</title>
  <link href="output.css" rel="stylesheet">
</head>
<body class="bg-gray-100 text-center p-10">
  <h1 class="text-4xl font-bold text-blue-600">Hello Tailwind!</h1>
</body>
</html>
"""
pname=input("Enter the name of your project folder: ")
try:
    os.mkdir(f"C:\\users\\{user_name}\\Downloads\\{pname}")
except:
    pass
os.chdir(f"C:\\users\\{user_name}\\Downloads\\{pname}")

def setup():
    subprocess.run(["npm", "init", "-y"], shell=True)
    subprocess.run(["npm", "install", "-D", "tailwindcss"], shell=True)
    subprocess.run(["npx", "tailwindcss", "init"], shell=True)
    with open("input.css","w") as f:
        f.writelines('''@import "tailwindcss";''')
    with open("index.html","w") as f:
        f.write(body_text)
    subprocess.run(["npx", "@tailwindcss/cli", "-i", "./input.css", "-o", "./output.css"], shell=True)
    time.sleep(2)
    subprocess.run(["code", "."], shell=True)
    webbrowser.open_new_tab(f"C:\\users\\{user_name}\\Downloads\\{pname}\\index.html")
def installer():
    subprocess.run([
    "powershell", "-Command",
    "Invoke-WebRequest -Uri https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi -OutFile nodejs.msi"
])
    subprocess.run(["msiexec", "/i", "nodejs.msi", "/quiet", "/norestart"])
def check_node_installed():
    try:
        subprocess.run(['node', '-v'], capture_output=True, text=True, check=True)
        setup()
    except :
        installer()
        setup()

check_node_installed()
