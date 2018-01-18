import datetime

from google.cloud import datastore


def create_client(project_id):
    # current_app.config['PROJECT_ID']
    return datastore.Client(project_id)

def add_user(client, dict_user):
    key = client.key('User')

    user = datastore.Entity(
        key) #, exclude_from_indexes=['password']

    user.update({
        'created': datetime.datetime.utcnow(),
        'first_name': dict_user['first_name'],
        'last_name': dict_user['last_name'],
        'email':dict_user['email'],
        'password':dict_user['password']
    })

    client.put(user)

    return user.key

def get_user(client,email,password):
    query = client.query(kind='User')
    query.add_filter('email', '=', email)
    query.add_filter('password', '=', password)

    result = list(query.fetch())
    return next(iter(result or []), None)

def basic_query(client, user_id):
    with client.transaction():
        key = client.key('User', user_id)
        user = client.get(key)

        if not user:
            raise ValueError(
                'User {} does not exist.'.format(user_id))

        user['done'] = True

        client.put(user)