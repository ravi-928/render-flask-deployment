from markett import app, db
from markett.models import Item, User

with app.app_context():
    item = Item.query.filter_by(name='Lenovo Thinkpad').first()
    print(item.owner)  # This gives the owner's user ID

    if item.owner:
        owner = User.query.get(item.owner)
        print(owner.username)
    else:
        print("Item is on the market, no owner.")
