import os


import crud
import model
import server

os.system("dropdb kickback")
os.system("createdb kickback")

if __name__ == "__main__":
    
    model.connect_to_db(server.app)
    server.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    


    model.db.create_all()

    guest = crud.create_guest_user('sara', 'stevens', 'Sara.5029', 'sarastevens123@gmail.com')
    model.db.session.add(guest)
    model.db.session.commit()

    restaurant = crud.create_restaurant_user('test', 'test', 'test', 'test')
    model.db.session.add(restaurant)
    model.db.session.commit()

    guest_review = crud.create_guest_review(guest.id, restaurant.id, '5', 'text', 'img')
    model.db.session.add(guest_review)
    model.db.session.commit()

    restaurant_review = crud.create_restaurant_rating(guest.id, restaurant.id, '3', 'text', 'img')
    model.db.session.add(restaurant_review)
    model.db.session.commit()