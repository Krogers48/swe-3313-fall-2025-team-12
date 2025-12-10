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

Email Receipt:
- The application can send real email receipts using a Gmail account.
- This is optional: if email is not configured, the application will still work and show an on-screen receipt.
- We used the Gmail account: codebreakers.co@gmail.com with a Gmail App Password (not the normal account password).

- To enable email sending, set these environment variables before running the app:

  - SMTP_SERVER = smtp.gmail.com
  - SMTP_PORT   = 587
  - SMTP_USER   = codebreakers.co@gmail.com
  - SMTP_PASSWORD = <Gmail App Password>
  - SMTP_FROM   = codebreakers.co@gmail.com

- On Windows PowerShell, example:

  - $env:SMTP_SERVER="smtp.gmail.com"
  - $env:SMTP_PORT="587"
  - $env:SMTP_USER="codebreakers.co@gmail.com"
  - $env:SMTP_PASSWORD="qlxi hcvi byfv mpam"
  - $env:SMTP_FROM="codebreakers.co@gmail.com"

- After setting these, start the app normally:

  - cd source
  - env\Scripts\activate
  - python main.py

- When you complete Checkout with a valid email address, the application will:
  - Create an order,
  - Show an on-screen receipt,
  - Attempt to send an email receipt to the email entered at checkout (including order details, shipping address, and last four digits of the card).

- Activate the virtual environment:
Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate

(if Flask error)

- Install required dependencies:
python -m pip install flask
pip install flask passlib

- Run:
python main.py

- Open:
http://127.0.0.1:5000/

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

- If dependencies are missing, install them again:
  pip install -r source/requirements.txt

- If the virtual environment will not activate on Mac/Linux:
  chmod +x env/bin/activate
  source env/bin/activate

- If modules cannot be found, make sure you are inside the "source" directory before starting the app.

- If port 5000 is already in use:
  Mac/Linux:
    lsof -i :5000
    kill <PID>
  Windows:
    netstat -ano | findstr :5000
    taskkill /PID <PID> /F

- If the application cannot read or write database.json:
  - Make sure the file is not opened in another editor or program.
  - Make sure the JSON is valid. Use a validator such as https://jsonlint.com/.
  - Ensure the app is started from inside the "source" directory so the relative file path works correctly.

- If changes to the inventory or orders do not save:
  - Confirm the app has write permissions to the project directory.
  - Ensure you are not running the app from a read-only folder.
  - Make sure the virtual environment is active so Flask uses the correct working directory.

- If the application crashes after editing the JSON file:
  - Restore the original database.json from version control.
  - Verify that all brackets {} and arrays [] are correctly matched.