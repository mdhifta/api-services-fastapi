from sqlalchemy.orm import Session
from app.models.users import Users
from app.schema.users import UserSchema

# get all data users
def getUsers(db: Session, offsite:int=0, limit:int=0):
    return db.query(Users).offset(offsite).limit(limit).all()

# select by id
def getById(db: Session, user_id: int):
    return db.query(Users).filter(Users.user_id == user_id).first()

# create users
def createUser(db: Session, user: UserSchema):
    _user = Users(
        fname=user.fname,
        lname=user.lname,
        phone_number=user.phone_number,
        email=user.email,
        password=user.password,
        roles=user.roles
    )

    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

# delete users
def deleteUser(db: Session, user_id: int):
    _user = getById(db=db, users_id=user_id)

    db.delete(_user)
    db.commit()

# update users lname, fname and phone number
def updateUsers(db: Session, user_id:int, data:map):
    _user = getById(db=db, users_id=user_id)
    _user.fname = data.fname
    _user.lname = data.lname
    _user.phone_number = data.phone_number

    db.commit()
    db.refresh(_user)
    return _user