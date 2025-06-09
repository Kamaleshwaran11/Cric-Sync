import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER', 'root')}:{os.getenv('MYSQL_PASSWORD', 'Sk@3117')}@"
        f"{os.getenv('MYSQL_HOST', 'localhost')}/{os.getenv('MYSQL_DB', 'unstoppablescc')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
