from sqlalchemy.orm import subqueryload, joinedload

from dal_opt.db import  session_factory, User

session = session_factory()

users = session.query(User).filter(User.id.in_([1, 2]))
# users = session.query(User).filter(User.id.in_([1, 2])).options(joinedload('emails'))

for u in users:
    print('# user: ', u.first_name, ' ', u.last_name)
    for email in u.emails:
        print('# email: ', email.address)