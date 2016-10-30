from sqlalchemy.orm import subqueryload, joinedload

from dal_opt.db import session_factory, User

session = session_factory()

users = session.query(User).filter(User.id.in_([1, 2, 3]))
# users = session.query(User).filter(User.id.in_([1, 2, 3])).options(joinedload('emails'))
# users = session.query(User).filter(User.id.in_([1, 2, 3])).options(subqueryload('emails'))

for u in users:
    print('# user: ', u.first_name, ' ', u.last_name)
    for email in u.emails:
        print('# email: ', email.address)
