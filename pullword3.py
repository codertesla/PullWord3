import requests

# pullword function, set default treshold to 0.8
def pullword(sentence,Threshold=0.8,Debug=1,json=1):
    url = 'http://api.pullword.com/get.php' # PullWord API
    payload = {
        'source' : sentence,
        'param1' : Threshold,
        'param2' : Debug,
        'json' : json
    }
    try:
        r = requests.get(url,params=payload,timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error':str(e)}
    