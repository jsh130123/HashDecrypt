# Made By 정승환
# ProjectName: Rainbow Table을 이용한 해시 복호화.

import requests
from bs4 import BeautifulSoup

def hashIdentifier(hash):
    hashLen = len(hash)

    if hashLen == 32:
        return "md5"
    elif hashLen == 40:
        return "sha1"
    else:
        return False
    
def md5Decrypt(hash):
    res = requests.get(f"https://md5.gromweb.com/?md5={hash}", headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    })
    soup = BeautifulSoup(res.text, "html.parser")
    decryptHash = soup.select_one('#string').get("value")

    return decryptHash
    
def sha1Decrypt(hash):
    res = requests.get(f"https://sha1.gromweb.com/?hash={hash}", headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    })
    soup = BeautifulSoup(res.text, "html.parser")
    decryptHash = soup.select_one('#string').get("value")

    return decryptHash

hash = input("Input Hash: ")
hashType = hashIdentifier(hash)

if hashType == "md5":
    decryptHash = md5Decrypt(hash)
    print(f"Found! Type: {hashType} DecryptHash: {decryptHash}")
elif hashType == "sha1":
    decryptHash = sha1Decrypt(hash)
    print(f"Found! Type: {hashType} DecryptHash: {decryptHash}")
else:
    print("Unknown hash!")