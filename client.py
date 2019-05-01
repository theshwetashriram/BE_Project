import socket                

def getRecommendations(userid,citylist):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost',2000))
    req=[userid]+citylist
    req=[str(x) for x in req]
    reqstr=",".join(req)
    s.send(str.encode(reqstr))
    s.send(str.encode('\n'))
    r=s.recv(100)
    response:str=r.decode('utf-8')
    response=response.strip().split(',')
    response=[int(x) for x in response]
    print(response)
    return response

if __name__=="__main__":
    getRecommendations(1,[2,3,4])