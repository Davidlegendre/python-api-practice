from models.User import User_Model
def get_item(id: int, user_bd: list[User_Model]) -> User_Model | None:
    for user in user_bd:
        if(user.id == id):
            return user
    return None
