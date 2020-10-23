from model import db, Person
from datetime import datetime

man1 = Person(
    'Taro',
    '090-6666-5555',
    12,
    datetime.now(),
    datetime.now(),
)
man2 = Person(
    'Jiro',
    '090-4444-4444',
    13,
    datetime.now(),
    datetime.now(),
)
man3 = Person(
    'Saburo',
    '090-3333-3333',
    14,
    datetime.now(),
    datetime.now(),
)
# db.session.add_all([man1, man2, man3])
# db.session.commit()

# print(Person.query.get(1))
# print(Person.query.first())

# for x in Person.query.filter(Person.name.endswith('o')).limit(2).all():
#     print(x)

# Person.query.filter_by(id=1).delete()
# db.session.commit()

Person.query.filter_by(name='nanashi').update(
    {
        'name': 'John',
        'update_at': datetime.now()
    }
)
db.session.commit()
