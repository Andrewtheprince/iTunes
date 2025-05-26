from database.DB_connect import DBConnect
from model.album import Album

class DAO:

    @staticmethod
    def getAlbums(dMin):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT a.AlbumId, a.Title, a.ArtistId, sum(t.Milliseconds)/1000/60 as dTot
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

    @staticmethod
    def getAllEdges(idMapAlbum):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT DISTINCTROW t1.AlbumId as a1, t2.AlbumId as a2
                    FROM track t1, track t2, playlisttrack p1, playlisttrack p2
                    WHERE t2.TrackId = p2.TrackId and t1.TrackId = p1.TrackId and p2.PlaylistId = p1.PlaylistId
                    and t1.AlbumId < t2.AlbumId"""
        cursor.execute(query)
        for row in cursor:
            if row["a1"] in idMapAlbum and row["a2"] in idMapAlbum:
                result.append((idMapAlbum[row["a1"]], idMapAlbum[row["a2"]]))
        cursor.close()
        conn.close()
        return result
