from app import app,db,Student

with app.app_context():
    db.create_all()

    nicole=Student('Nicole',45,'Female',300)
    joshua=Student('Joshua',2,'Male',5)
    albert=Student('Albert',12,'Male',90)
    herbert=Student('Herbert',32,'Male',87)
    caleb=Student('Caleb',78,'Male',4)
    jalilu=Student('Jalilu',39,'Male',57)
    pokua=Student('Pokua',15,'Female',78)
    db.session.add_all([nicole,joshua,albert,herbert,caleb,jalilu,pokua])
    db.session.commit()