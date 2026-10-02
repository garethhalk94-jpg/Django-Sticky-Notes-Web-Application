### Django Sticky Notes Web Application: Part 1
A web based, sticky note application for users to leave un/anonymous notes for one another in a contained environment
Users can see view specifics of note details, like what time and date that notes were stuck to the board, and can add,
remove, and modify notes on the board.

### 1. System Requirements & Context
* **Python Runtime Engine:** Version 3.11+ or 3.14 recommended.
* **Core Application Framework:** Django 5.0+ / 6.0+ Web Registry Engine.
* **Local Workspace DB Store:** SQLite Embedded Subsystem (`db.sqlite3`).
* **Design Presentation Layer:** Bootstrap 5 Integration Framework combined with custom handwriting typography.

### 2. Operational Step-by-Step Launch Sequence
To initialize, sync, and deploy this project workspace smoothly on a local machine, execute these terminal commands in order:

```bash
# Initialize virtual environment
python -m venv myenv

# Activate the local virtual environment wrapper
# On Windows Command Prompt:
myenv\Scripts\activate
# On macOS / Linux Terminal:
source myenv/bin/activate

# Install deployment dependencies
pip install -r requirements.txt

# Make migration file and apply them
python manage.py makemigrations notes
python manage.py migrate

# Boot up the interactive local development engine server
python manage.py runserver
```

Once running, launch a web browser window and open the dashboard entry portal:
`http://127.0.0.1:8000/`


### 3. Testing
To run project tests:
```bash
python manage.py test notes
```
