## Healthcare Management Web Application

## Project Description:

This is a Healthcare Management Web Application built using Django.
It provides separate dashboards for patients and doctors, ensuring a personalized experience after login.

🔹 Patients can sign up, log in, upload a profile picture, and view their dashboard with personal details.

🔹 Doctors can log in and access their own dashboard with doctor-specific details.

🔹 Secure authentication is implemented using Django’s built-in user model (extended with custom fields).

🔹 Profile pictures, addresses, and user roles (Doctor/Patient) are supported.

🔹 Frontend is styled with CSS for a clean, responsive interface.

## Tech Stack:

Python (Django Framework)

HTML, CSS

SQLite3 (default Django DB)

Pillow (for image uploads)

## How to Run the Application:

1) Clone the repository:

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name


2) Create a virtual environment and activate it:

    python -m venv venv
    venv\Scripts\activate   # (on Windows)


3) Install dependencies:

    pip install -r requirements.txt


4) Run migrations:

    python manage.py makemigrations
    python manage.py migrate


5) Create a superuser (admin account):

    python manage.py createsuperuser


6) Run the server:

    python manage.py runserver


7) Open in browser:

    http://127.0.0.1:8000



