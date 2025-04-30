from database.DB_connect import DBConnect
from model import airport
from model.airport import Airport
from model.flight import Flight


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroports():
        """Restituisce tutti gli aeroporti presenti nel database"""
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getEdges(distanzaMinima):
        """Restituisce soltanto le coppie di aeroporti collegati da una distanza pari alla distanzaMinima passata come input"""
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) as d
                    from flights f
                    group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID
                    having AVG(DISTANCE)>%s"""

        cursor.execute(query, (distanzaMinima,))

        for row in cursor:
            result.append(Flight(row['ORIGIN_AIRPORT_ID'], row['DESTINATION_AIRPORT_ID'], float(row['d'])))

        cursor.close()
        conn.close()
        return result


if __name__ == '__main__':
    print(DAO.getEdges(4000))