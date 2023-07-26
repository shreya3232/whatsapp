import requests
def sendWSP(message, apikey,gid=0):
    url = "https://whin2.p.rapidapi.com/send"
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": "whin2.p.rapidapi.com"}
    try:
        if gid==0:
            return requests.request("POST", url, json=message, headers=headers)
        else: 
            url = "https://whin2.p.rapidapi.com/send2group"
            querystring = {"gid":gid}
            return requests.request("POST", url, json=message, headers=headers, params=querystring) 
    except requests.ConnectionError:
        return("Error: Connection Error")

# Testing Section
msg1 = {"text":"hello there"}
msg2 = {"text":"this is a group message"}

myapikey = "3ca735ec8emshcf02d10275006c8p1e31c1jsn5373f14fdf3f"
mygroup = "KZkdX4l7XJX5qAoxoN6RCU"

sendWSP(msg1,myapikey)
sendWSP(msg2, myapikey,mygroup)