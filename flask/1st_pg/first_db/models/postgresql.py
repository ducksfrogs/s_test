"""
instance/postgresql.py
"""

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'test',
    'password': 'yama2376',
    'host': '127.0.0.1',
    'name': 'test'
})