import urllib.request
def connect(host='https://youtube.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


if connect():
    print("connected")
else:
    print("no internet")
    
