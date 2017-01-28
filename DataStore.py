#!/usr/local/bin/python3.4
import requests
import json
import urllib.parse


def uploadFile(file, mimeType, data):
    mimeType = urllib.parse.quote_plus(mimeType)
    r = requests.post("http://192.168.1.14/upload.php?mimeType=" + mimeType, files={
        "file": file,
    }, data={
        "data": json.dumps(data)
    })
    ret = json.loads(r.text)
    return (ret["result"] == "success", ret)

def getIds(conditions):
    maxId = 0
    idList = []

    while True:
        r = requests.post("http://192.168.1.14/", data=json.dumps({
            'metaIdMax': maxId,
            'conditions': conditions
        }))
        ret = json.loads(r.text)
        if ret["result"] != "success" or len(ret["imageIds"]) == 0:
            break
        idList += ret["imageIds"]
        maxId = ret["metaIdMax"]

    return idList




if __name__ == '__main__':
    print(len(getIds([
        "comp platform =tinder_profiles"
    ])))