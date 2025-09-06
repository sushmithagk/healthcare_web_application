## Healthcare Management Web Application

## Project Description:

This is a Healthcare Management Web Application built using Django.

 * Separate dashboards for Patients and Doctors for personalized experiences.

 * Patients: Sign up, log in, upload profile picture, and view personal dashboard.

 * Doctors: Log in and access doctor-specific dashboard.

 * Authentication: Secure login using Django’s built-in user model (extended with custom fields).

 * Support for profile pictures, addresses, and user roles (Doctor/Patient).

 * Clean, responsive interface styled with CSS.

 ## Integrated Blog System

 * Doctors can create and upload blog posts under categories such as Mental Health, Heart Disease, Covid19, Immunization.

 * Blog post form includes: Title, Image, Category, Summary, Content.

 * Doctors can mark posts as drafts; view all their uploaded posts.

 * Patients can view all published posts, organized by category.

 * Blog listings display: Title, Image, Summary (truncated to 15 words if longer).

## Tech Stack:

Python (Django Framework)

HTML, CSS

MYSQL (database)

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



