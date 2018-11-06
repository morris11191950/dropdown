from app import db


class Districts():

    def __init__(self):
        try:
            conn = db.connect()
        except cursor.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        self.conn = conn

    def districts(self):
        districts = []
        ids = []
        cursor = self.conn.cursor()
        sql = """SELECT district_id, district_name from district"""
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        for row in rows:
            ids.append(row)
            districts.append(row)
        return districts
