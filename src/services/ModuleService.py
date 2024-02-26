from src.models.db import db
from src.models.module import Module

def add(data):

    new_module = Module()

    for key, value in data.items():
        if hasattr(new_module, key):
            print(key)
            setattr(new_module, key, value)

    db.session.add(new_module)
    db.session.commit()


    return new_module

def get_by_id(module_id) -> Module:

    queried_module = Module.query.get(module_id)


    return queried_module

def get_all() -> [Module]:

    modules = Module.query.all()


    return modules

def delete(module_id) -> Module:

    module = Module.query.get(module_id)
    # handles cascading deletes while avoiding the issues with sqlalchemy 
    # doesnt do cascades well 
    for quiz in module.quizzes:
        db.session.delete(quiz)
    for lesson in module.lessons:
        db.session.delete(lesson)
    for user_module in module.user_modules:
        db.session.delete(user_module)
    db.session.delete(module)
    db.session.commit()


    return module