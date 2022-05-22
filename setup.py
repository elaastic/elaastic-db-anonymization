from setuptools import setup

setup(
    name='elaastic-db-anonymization',
    version='0.0.1',
    packages=['elaastic', 'elaastic.db', 'elaastic.db.anonymization'],
    url='',
    license='affero GPL v3',
    author='',
    author_email='',
    description='Elaastic DB anonymisation script',
    install_requires=[
        'faker',
        'gender_guesser',
        'mysql.connector',
        'unidecode'
    ]
)
