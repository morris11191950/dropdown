from app import db
#from flask import jsonify

class Queries():

    def __init__(self):
        try:
            conn = db.connect()
        except cursor.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        self.conn = conn

    def references(self, district_id):
        json_refs = []
        cursor = self.conn.cursor()
        sql = """SELECT r.reference_id, r.reference
            FROM reference r
            INNER JOIN district_to_reference d ON d.reference_id = r.reference_id
            WHERE d.district_id = %s"""
        cursor.execute(sql, district_id)
        self.conn.close()
        rows = cursor.fetchall()
        #Convert to JSON format
        for row in rows:
            json_ref = {'reference_id': row[0], 'reference': row[1]}
            json_refs.append(json_ref)
            json_ref = {}
        return json_refs

    def districts(self):
        #districts = []
        #ids = []
        cursor = self.conn.cursor()
        sql = """SELECT district_id, district_name from district"""
        cursor.execute(sql)
        self.conn.close()
        rows = cursor.fetchall()
        # for row in rows:
        #     district.append(row[0])
        return rows
