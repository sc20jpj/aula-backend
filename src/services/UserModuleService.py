from src.models.db import db
from src.models.user_module import UserModule

def add(user_id,module_id) -> UserModule:


    
    new_user_module = UserModule(user_id=user_id,module_id=module_id)
    


    db.session.add(new_user_module)
    db.session.commit()


    return new_user_module
    