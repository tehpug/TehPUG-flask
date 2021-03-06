from setuptools import setup

setup(name='TehPUG',
    version='0.1',
    description='TehPUG Website',
    author='Mehdy Khoshnoody, Keyvan Hedayati',
    author_email='mehdy.khoshnoody@outlook.com, k1.hedayati93@gmail.com',
    url='https://github.com/tehpug/TehPUG',
    install_requires=['Flask==0.10.1', 'Flask-Login==0.2.9',
                      'Flask-SQLAlchemy==1.0', 'Flask-WTF==0.9.4',
                      'Jinja2==2.7.2', 'Khayyam==0.9.2', 'MarkupSafe==0.18',
                      'SQLAlchemy==0.9.3', 'Tempita==0.5.2', 'WTForms==1.0.5',
                      'Werkzeug==0.9.4', 'decorator==3.4.0',
                      'itsdangerous==0.23', 'pbr==0.6',
                      'sqlalchemy-migrate==0.8.5', 'wsgiref==0.1.2'],
)
