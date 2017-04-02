import peewee as pw
import os
from time import sleep

vehicle_id="101"

db=pw.SqliteDatabase("admin")
db.connect()
db.execute_sql("""create table admin_cards(
                id varchar(100) primary key NOT NULL,
                purpose varchar(40) NOT NULL
                );""")
atr=os.popen("node card2.js").read().split('\n')

while atr[0]!="card inserted":
    atr=os.popen("node card2.js").read().split('\n')
    continue
print(atr)
print(" added as addition card")

db.execute_sql("""insert into admin_cards values('%s','add')"""%atr[1])

comp=False
while not comp:
    atr=os.popen("node card2.js").read().split('\n')
    while atr[0]!="card inserted":
        atr=os.popen("node card2.js").read().split('\n')
        continue
    print(atr)

    try:
        db.execute_sql("""insert into admin_cards values('%s','delete')"""%atr[1])
        print(atr)
        print(" added as deletion card")
        comp=True
    except:
        print("Already registered card")
        sleep(2)

db.close()
