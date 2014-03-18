import os

CSRF_ENABLED = True
SECRET_KEY = 'TehPug-Secure-Key'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
