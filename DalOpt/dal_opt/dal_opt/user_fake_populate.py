from dal_opt.db import session_factory, GoodUser, BadUser

from faker import Faker
import uuid

session = session_factory()

for x in range(100000):
    f = Faker()
    name = f.name()
    address = f.address()
    comment = f.text()

    id = uuid.uuid4()
    bad_user = BadUser(id=str(id),
                        name=name,
                        address=address,
                        comment=comment)

    good_user = GoodUser(id=id,
                        name=name,
                        address=address,
                        comment=comment)

    session.add(bad_user)
    session.add(good_user)
    session.commit()