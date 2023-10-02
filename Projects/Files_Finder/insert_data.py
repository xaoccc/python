import pathlib
import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='files_finder',
    user='postgres',
    password=''
)

cur = con.cursor()

data = cur.fetchall()

# Get all files and folder from specific path. Don't forget to change directory separator from \ to / !
files = pathlib.Path('C:/Users/user/Documents')

# Recursively get all files from directory inside files and filter it by extension (in this case mp3).
#  If you want all files use '*' as filter parameter inside rglob.
filtered_data = list(files.rglob('*.xlsx'))

# loop through the data
for f in filtered_data:

    file_name = f.parts[-1][:-5]
    file_path = '\\'.join(f.parts[:-1])
    query = '''INSERT INTO files(file_name, file_path)
            VALUES
                (%s, %s, %s)
            '''
    cur.execute(query, (file_name, file_path))
con.commit()
