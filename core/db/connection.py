from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

url_object = URL.create(
    "postgresql",
    username="postgres",
    password="artmy278",  # plain (unescaped) text
    host="db",
    database="db",
    port=8001
)

# engine = create_engine("postgresql://postgres:atemy278@db:8101/db")

# Database access
engine = create_engine(url_object)

# Interactions with database
Session = sessionmaker(bind=engine)
session = Session()

# This function was created for connection testing
"""def check():
    client = session()
    try:
        result = client.execute(text('select 1'))
        for row in result:
                print(row)
    except Exception as eror:
        print(str(eror))

check()"""
