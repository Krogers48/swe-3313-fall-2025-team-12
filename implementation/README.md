# Implementation  

This document explains how to set up, run, and troubleshoot the Circuit Breakers Radar Store application. Follow these steps to ensure the system runs correctly on any machine.
---  

## Environment Setup  
- Install Python 3.10 or higher.
Download from: https://www.python.org/downloads/

- Verify installation:
python3 --version
or on Windows:
python --version

- Create a virtual environment:
python3 -m venv env

- Activate the virtual environment:
Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate

- Install required dependencies:
pip install -r source/requirements.txt

- No additional tools or IDEs are required. A basic terminal is enough.
---  
  
## Data Storage Setup  
- All persistent data is stored in source/database.json.

- The JSON file contains:

- Users

- Administrator accounts

- Inventory records

- Orders

- Purchased inventory items

- Order-to-item relationships

- The project includes complete seed data:

- One administrator account

- Multiple customer accounts

- A full radar inventory list

- Example order history

- No database server or additional setup is needed.

- All purchases permanently update database.json, and purchased inventory stays removed even after restarting the application.
---  
  
## How to Start  
- Open a terminal and navigate to the project folder.

- Move into the source directory:
cd source

- Run the application:
python main.py
or
python3 main.py

- Open a browser and go to:
http://localhost:5000

- The login screen will load automatically.

- Sample login credentials included in the seed data:

admin / admin123! (Administrator)

User001 / strngp@55w0rd (Customer)

User002 / un6355@ble (Customer)

---  
  
## Troubleshooting  
- If Flask is missing, reinstall dependencies:
pip install -r source/requirements.txt

- If the virtual environment will not activate on Mac/Linux:
chmod +x env/bin/activate
source env/bin/activate

- If modules cannot be found, confirm you are inside the source directory before running the app.

- If port 5000 is already in use:

Mac/Linux:
lsof -i :5000
kill <PID>

Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

- If changes to database.json do not save, make sure the application was started from inside the source directory.
