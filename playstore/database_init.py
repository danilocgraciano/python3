import MySQLdb
print('Connecting...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)

conn.cursor().execute("DROP DATABASE `playstore`;")
conn.commit()

create_tables = '''SET NAMES utf8;
    CREATE DATABASE `playstore` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `playstore`;
    CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `device` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(50) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(create_tables)

# inserting users
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO playstore.user (id, name, password) VALUES (%s, %s, %s)',
      [
            ('primo', 'Primo', '123456'),
            ('danilocgraciano', 'Danilo C. Graciano', '123456')
      ])

cursor.execute('select * from playstore.user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserting games
cursor.executemany(
      'INSERT INTO playstore.game (name, category, device) VALUES (%s, %s, %s)',
      [
            ("pou", "kids", "Moto G2"),
            ("subway surfers", "kids", "Moto G3"),
            ("my talking tom", "kids", "Moto G3"),
            ("despicable me", "kids", "iPhone"),
            ("zombie tsunami", "kids", "iPhone"),
      ])

cursor.execute('select * from playstore.game')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
    print(game[1])

# commit
conn.commit()
cursor.close()