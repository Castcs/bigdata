# Salary vs. Cost of Living for Software Developers

This is a Flask-based backend, Vue3 front-end application for Big Data Analytics at East Carolina University.

Team Members: Aaron Thomas, Cameron Stiver, Madeleine Saucier

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- PostgreSQL
- Node package manager
- Vue 3.0

### Setting Up a Virtual Environment

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Castcs/bigdata.git
```
2. Navigate to the backend folder

	In a terminal, type BigDataVenv\Scripts\activate and press enter.

3. Installing backend dependencies

	In the same terminal, with the virtual environment launched, type "pip install -r requirements.txt"
	This will install all of the required depencies for the backend within your virtual environment. Leave this terminal open as we will need it to create the database tables.

### Setting up the Postgres Database

1.  The application requires your user is named: postgres, with password: admin.  If this is not true for you, then you will need to change
	the services.config file located within the backend folder with the correct username and password information.

2.  In PGAdmin, create a new database called BigData.

3.  After this, in the terminal from setting up the virtual environment, type "flask run".  This will automatically create the tables required for the application if the tablename, username, and password are all correct.

4.  After the backend is launched, you can then take the three CSVs that came with this repository to upload into the corresponding tables.