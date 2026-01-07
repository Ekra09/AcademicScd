# config.py

class Config:
    # Replace with your own values
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1101@localhost/AcademicDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'  # Needed for sessions, CSRF protection, etc.
