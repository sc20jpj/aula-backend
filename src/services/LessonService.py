from src.models.db import db
from src.models.lesson import Lesson

def add(data,module_id):

    new_lesson = Lesson(module_id=module_id)

    for key, value in data.items():
        if hasattr(new_lesson, key):
            print(key)
            setattr(new_lesson, key, value)

    db.session.add(new_lesson)
    db.session.commit()


    return new_lesson

def get_by_id(id) -> Lesson:

    queried_lesson = Lesson.query.get(id)

    print(queried_lesson)
    return queried_lesson
def get_all() -> [Lesson]:

    lessons = Lesson.query.all()


    return lessons

def delete(lesson_id) -> Lesson:

    lesson = Lesson.query.get(lesson_id)

    db.session.delete(lesson)
    db.session.commit()


    return lesson