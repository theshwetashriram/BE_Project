import mysql.connector


class Database():

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="travel"
        )

    def close(self):
        self.db.commit()
        self.db.close()

    def commit(self):
        self.db.commit()

    def getCursor(self):
        return self.db.cursor()

    def getStates(self):
        cursor=self.getCursor()
        cursor.execute("select * from state")
        result=cursor.fetchall()
        cursor.close()
        return result

    def getStateById(self,stateid):
        cursor=self.getCursor()
        cursor.execute("select * from state where stateid="+str(stateid))
        result=cursor.fetchall()
        cursor.close()
        return result[0]

    def getCities(self, stateid):
        cursor=self.getCursor()
        cursor.execute("select * from city where stateid="+str(stateid))
        result=cursor.fetchall()
        cursor.close()
        return result           

    def getCityById(self,id):
        cursor=self.getCursor()
        cursor.execute("select * from city where id="+str(id))
        result=cursor.fetchall()
        cursor.close()
        return result[0]

    def getplaces(self, placeid):
        cursor=self.getCursor()
        cursor.execute("select * from place where placeid="+str(placeid))
        result=cursor.fetchall()
        cursor.close()
        return result       

    def checkLogin(self, username, password):
        cursor=self.getCursor()
        cursor.execute("select * from members where username=%s and password=%s",(username,password))
        result=cursor.fetchall()
        # for x in result:
        #     print(x)        
        id=-1
        if len(result)>0:
            id=result[0][0]
        cursor.close()
        return id

    # def addCity(self,name):
    #     print('adding city ',name)
    #     #insert into city
    #     cursor=self.getCursor()
    #     cursor.execute("insert into city values(0, '"+name+"')")
    #     # result=cursor.fetchall()
    #     cursor.close()

    def addPlacetag(self,state,city):
        #insert into city
        cursor=self.getCursor()
        cursor.execute("insert into city values(%d, %s)" , (placetag , tag))
        # result=cursor.fetchall()
        cursor.close()   

    def addState(self, name):
        print('adding state ',name)
            #insert into place
        cursor=self.getCursor()
        cursor.execute("insert into State values(0, '"+name+"')")
        cursor.close()


    def addPlace(self,place, desc, longitude, latitude, cityid):
            #insert into city
        cursor=self.getCursor()
        cursor.execute("insert into place values(0,%s, %s, %s, %s, %s)", (place,desc,longitude,latitude,cityid))
        cursor.close()

    def addPlacetag(self, placeid, name):
            #insert into placetag
        cursor=self.getCursor()
        cursor.execute("insert into place_tag values(%d,%s)", (placeid,name))
        cursor.close

    def addCity(self, name,stateid,desc, longitude, latitude,cityid):
        print('adding state ',name)
        cursor=self.getCursor()
        cursor.execute("insert into city values(0,%s, 0,%s, %s, %s, %s)", (cityid,name,stateid,desc,longitude,latitude))
        cursor.close()

    