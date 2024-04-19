from faker import Faker

from models.database import create_db, Session
from models.models import Order, Courier, District


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    districts = ['Центральный', 'Индустриальный', 'Ленинский', 'Железнодорожный']

    order1 = Order(name='Роллы')
    order2 = Order(name='Макароны')
    order3 = Order(name='Рыба')

    session.add(order1)
    session.add(order2)
    session.add(order3)

    for key, dist in enumerate(districts):
        district = District(name=dist)
        district.orders.append(order1)
        if key % 2 == 0:
            district.orders.append(order2)
        district.add(district)

    session.commit()

    fake = Faker('ru_RU')
    orders = [order1, order2]

    for _ in range(10):
        name = fake.name()
        order = fake.random.choice(orders)
        session.add(name, order)

    session.commit()
    session.close()
