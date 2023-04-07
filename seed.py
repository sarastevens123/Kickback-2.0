import os
import crud
import model
from server import app


os.system("dropdb kb")
os.system("createdb kb")


if __name__ == "__main__":
    print("***************************connected to __main__****************************")
    model.connect_to_db(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    print("***************************connected to database****************************")
    


    model.db.create_all()
    print("***********************created all from db***************")

    guest = crud.create_guest_user('sara', 'stevens', 'Sara.5029', 'sarastevens123@gmail.com')
    model.db.session.add(guest)
    model.db.session.commit()

    restaurant = crud.create_restaurant_user('test', 'test', 'test', 'test')
    model.db.session.add(restaurant)
    model.db.session.commit()

    guest_review = crud.create_guest_review(guest.id, restaurant.id, '5', 'text')
    model.db.session.add(guest_review)
    model.db.session.commit()

    restaurant_review = crud.create_restaurant_review(guest.id, restaurant.id, '3', 'text')
    model.db.session.add(restaurant_review)
    model.db.session.commit()