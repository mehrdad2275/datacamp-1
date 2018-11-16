'''
Filter data selected from a Table - Advanced

You're really getting the hang of this! SQLAlchemy also allows users to use conjunctions such as and_(), or_(), and not_() to build more complex filtering. For example, we can get a set of records for people in New York who are 21 or 37 years old with the following code:

|   stmt([census]).where(
|     and_(census.columns.state == 'New York',
|          or_(census.columns.age == 21,
|             census.columns.age == 37
|            )
|         )
|     )
'''

from sqlalchemy import create_engine, select, MetaData, Table

# DataCamp PostgreSQL on AWS does not acceppt remote connections. Permission denied
# Local MySQL or SQLite may be used instead
#engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
engine = create_engine('mysql://root:@localhost:3306/circle')
#engine = create_engine('sqlite:///../datasets/census.sqlite')

connection = engine.connect()

metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)

'''
INSTRUCTIONS

*   Import and_ from the sqlalchemy module.
*   Select all records from the census table.
*   Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
*   Iterate over the ResultProxy and print the age and sex columns from each record.
'''

# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)

