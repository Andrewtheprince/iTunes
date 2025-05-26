from database.DB_connect import DBConnect
from model.album import Album

class DAO:

    @staticmethod
    def getAlbums(dMin):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT a.*, sum(t.Milliseconds)/1000/60 as dTot
                    FROM album a, track t
                    WHERE a.AlbumId = t.AlbumId
                    group by a.AlbumId
                    having dTot > %s"""
        cursor.execute(query, (dMin,))
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result
