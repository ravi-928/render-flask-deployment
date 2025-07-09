from markett import app, db
from markett.models import User

with app.app_context():
    User.query.filter(User.budget < 5000).delete()
    db.session.commit()
    print("Deleted all users with budget less than 5000.")
