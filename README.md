# User Authentication System

This project is a user authentication system built with Django, designed to use an external database for storing user credentials and information. The system includes functionalities for user registration, login, and homepage navigation.

## Features
- User registration with username, email, and password
- Secure user authentication
- Login and logout functionalities
- Responsive UI with a modern design
- External database support

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: External database (MySQL)
- **Deployment**: Local development server (127.0.0.1:8000)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- MySQL

### Steps
1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the database**
   - Update `settings.py` with your external database credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'your_db_host',
             'PORT': 'your_db_port',
         }
     }
     ```
5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```
6. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Usage
- Navigate to `http://127.0.0.1:8000/` to access the homepage.
- Click **Register** to create a new account.
- Click **Login** to authenticate and access the system.

## Screenshots
### Registration Page

![Screenshot 2025-02-16 233904](https://github.com/user-attachments/assets/817bacde-edf5-466e-be80-3caf20cf82f5)

### Login Page

![Screenshot 2025-02-16 233852](https://github.com/user-attachments/assets/46cc1f7b-060f-4253-bc68-9a3fddf3762f)

### Home Page

![Screenshot 2025-02-16 233832](https://github.com/user-attachments/assets/2598ef0e-12e9-4da1-aff3-fb2e124c1e23)

## Author
Developed by Richie Sayer

