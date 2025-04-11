# README for allMenMustDie-1

## Project Overview
allMenMustDie-1 is a Flask-based web application designed to mimic the gameplay of Tribal Wars. This project currently implements a user login system, allowing users to register and log in to their accounts.

## TODO

1. User Management:
- login
- logout
- register
- change password
- change username
- implement verification email in the distant future

2. Village management
- village view (resources, buildings and men)
- rename village 
- prepare buildings
- construct buildings
- make buldings meaningful (bonuses!)
- think about statistics sheet

3. Army management 
- different types of soldiers
- different statistics for each type
- recruit soldiers
- disband soldiers
- recruitment time

4. Map
- villages have to be on specific coordinates
- think about map design
- villages have to spawn with random coordinates
- army will march accordingly to distance

5. Scheduler
- how often does the game world updates?
- one or many schedulers (constant update each 10sec or different intervals for different mechanics)

## Project Structure
```
allMenMustDie-1
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   ├── templates
│   │   │   ├── auth
│   │   │   │   ├── login.html
│   │   │   │   ├── register.html
│   │   │   └── base.html
│   │   └── static
│   │       ├── css
│   │       │   └── style.css
│   │       └── js
│   │           └── main.js
│   ├── config.py
│   └── run.py
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd allMenMustDie-1
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

5. **Run the application**:
   ```
   python src/run.py
   ```

## Usage
- Navigate to `http://localhost:5000` in your web browser.
- You can register a new account or log in with an existing account.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.