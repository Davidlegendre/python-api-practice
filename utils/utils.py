from models.User import User_Model
def get_item_byDNI(dni: int, user_bd: list[User_Model]) -> User_Model | None:
    for user in user_bd:
        if(user.dni == dni):
            return user
    return None

def get_item_byId(id: int, user_bd: list[User_Model]) -> User_Model | None:
    for user in user_bd:
        if(user.id == id):
            return user
    return None