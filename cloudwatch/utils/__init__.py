from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(session_options={"autoflush":False})

# Flask migrate
migrate = Migrate()