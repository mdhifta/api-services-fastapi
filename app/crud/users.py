from sqlalchemy.orm import Session
from app.models.users import Users
from app.schema.users import UserSignUp
from passlib.context import CryptContext
from app.utils.generateNumber import Generate62

pwdHash = CryptContext(schemes=["bcrypt"], deprecated="auto")

# get all data users
def getUsers(db: Session, offsite:int=0, limit:int=0):
    return db.query(Users).offset(offsite).limit(limit).all()

# select by id
def getById(db: Session, user_id: int):
    return db.query(Users).filter(Users.user_id == user_id).first()

# validtaion email in query
def emailValidation(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

# create users
def createUser(db: Session, user: UserSignUp):
    _user = Users(
        fullname=user.fullname,
        phone_number=Generate62(user.phone_number),
        email=user.email,
        password=pwdHash.hash(user.password),
        roles=1
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

# update users fullname and phone number
def updateUsers(db: Session, user_id:int, data:map):
    _user = getById(db=db, users_id=user_id)
    _user.fullname = data.fullname
    _user.phone_number = data.phone_number

    db.commit()
    db.refresh(_user)
    return _user