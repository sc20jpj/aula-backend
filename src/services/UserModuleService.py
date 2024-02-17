from src.models.db import db
from src.models.user_module import UserModule

def add(user_id,module_id) -> UserModule:


    
    new_user_module = UserModule(user_id=user_id,module_id=module_id)
    


    db.session.add(new_user_module)
    db.session.commit()


    return new_user_module

def add_users(users,module_id) -> UserModule:
    

    new_user_modules = []
    for user in users:
        print(user)
        print(user["user_id"])
        new_user_module = UserModule(user_id=user["user_id"],module_id=module_id)
        new_user_modules.append(new_user_module)
        db.session.add(new_user_module)


    db.session.commit()


    return new_user_modules
    