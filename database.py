import mysql.connector
from itertools import permutations
from itinerary import Itinerary, ItineraryCity, ItineraryPlace


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

    def executeUpdate(self,query):
        cursor=self.getCursor()
        cursor.execute(query)
        cursor.close()

    def executeQuery(self,query):
        cursor=self.getCursor()
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.close()
        return result

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

    def getplaces(self, cityid):
        cursor=self.getCursor()
        cursor.execute("select * from place where cityid="+str(cityid))
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

    def register(self, username, fname, lname, password):
        cursor=self.getCursor()
        cursor.execute("insert into users value (0,%s,%s,%s,password(%s))",(username,fname, lname,password))

    def userlogin(self, username, password):
        cursor=self.getCursor()
        cursor.execute("select * from users where username=%s and password=password(%s)",(username,password))
        result=cursor.fetchall()
        return result


    def getlistdistance(self,citylist):
        distance=0
        for i in range(0,len(citylist)-1):            
            distance=distance+self.getdistance(citylist[i],citylist[i+1])
        return distance

    def getdistance(self,cityid1,cityid2):
        print('getdistance',cityid1,cityid2)
        cursor=self.getCursor()
        cursor.execute("select * from city where id=%s or id=%s",(cityid1,cityid2) )
        result=cursor.fetchall()
        lng1=result[0][4]
        lat1=result[0][5]
        lng2=result[1][4]
        lat2=result[1][5]
        distance=self.gcd(lng1,lat1,lng2,lat2)
        cursor.close()
        return distance

    def gcd(self,lon1, lat1, lon2, lat2):
        # print("%f %f %f %f" % (lon1,lat1,lon2,lat2))
        from math import radians, cos, sin, asin, sqrt
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    def findPlaces(self, cityid, locationtags):
        if not locationtags or len(locationtags)==0:
            return []
        cursor=self.getCursor()
        format_strings = ','.join(['%s'] * len(locationtags))
        q="select distinct place.* from place,place_tag where place.placeid=place_tag.placeid and place_tag.name in (%s) and cityid=%%s" % format_strings
        # print(q)
        cursor.execute(q,tuple(locationtags+[cityid]) )
        result=cursor.fetchall()
        cursor.close()
        return result


    def getItineraries(self, homecity, selectedcities, locationtags, minbudget, maxbudget):
        perms_0=list(permutations(selectedcities))

        perms=[]
        for p in perms_0:
            p2=[homecity]+list(p)+[homecity]
            perms.append(p2)
            if(2*len(perms)>=len(perms_0)):
                break

        print('perms',perms)

        distancelist=[]
        for p in perms:
            distance=self.getlistdistance(p)
            #distancemap[p]=distance
            distancelist.append([p,distance])

        itineraries=[]

        for k,v in distancelist:
            print(k,v)
            it=Itinerary()
            itineraries.append(it)
            it.distance=int(v)
            for i in range(1,len(k)-1):
                cityid=k[i]
                print('\t',cityid)
                city=ItineraryCity()
                db_city=self.getCityById(cityid)
                city.id=cityid
                city.description=db_city[3]
                city.longitude=db_city[4]
                city.latitude=db_city[5]
                city.name=db_city[1]
                it.citylist.append(city)
                print(len(it.citylist))

                places=self.findPlaces(cityid,locationtags)
                for db_place in places:
                    place=ItineraryPlace()
                    place.placeid=db_place[0]
                    place.name=db_place[1]
                    place.description=db_place[2]
                    place.longitude=db_place[3]
                    place.latitude=db_place[4]

                    city.placelist.append(place)

            #print(k,v)

        return itineraries

    # def addCity(self,name):
    #     print('adding city ',name)
    #     #insert into city
    #     cursor=self.getCursor()
    #     cursor.execute("insert into city values(0, '"+name+"')")
    #     # result=cursor.fetchall()
    #     cursor.close()

    # def addPlacetag(self,state,city):
    #     #insert into city
    #     cursor=self.getCursor()
    #     cursor.execute("insert into city values(%d, %s)" , (placetag , tag))
    #     # result=cursor.fetchall()
    #     cursor.close()   

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

    def addCity(self, name,stateid,desc, longitude, latitude):
        print('adding state ',name)
        cursor=self.getCursor()
        cursor.execute("insert into city values(0,%s,%s,%s, %s, %s)", (name,stateid,desc,longitude,latitude))
        cursor.close()

    