from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
from termcolor import colored
import os
import sys
import requests

path_of_chrome = ""

with open("path.txt", "r") as f:
    path_of_chrome = f.read().strip()

def save_stories_of_user(username):

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(path_of_chrome, options=options)

    flag = 5
    while flag > 0:
        
        try:
            print(colored("\n[INFO]: getting page of user: " + username+ ", attempts left: " + str(flag)+"\n", "yellow"))
            driver.get("https://insta-stories.online/"+username)
            print(colored("\n[SUCCESS]: page got, waiting stories", "green"))
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-item")))
            break
        except:
            print(colored("[ERROR]: waiting stories failed, attempts left: " + str(flag), "red"))
            flag -= 1

    if flag == 0:
        print(colored("[ERROR]: no stories found for user: " + username, "red"))
        return False

    count = 0
    content = driver.page_source
    soup = BeautifulSoup(content)
    for li in soup.findAll('li', attrs={'class': 'modal-item'}):
        div = li.find('div', attrs={'class': 'item'})
        img = div.find('a')
        data = img['data-title']
        dataType = img['data-type']
        extension = ".jpg" if dataType == 'image' else ".mp4"
        
        link = "https://insta-stories.online"+img['href']
        print(colored("\n[INFO]: getting story: " + data + " of user: " + username, "yellow"))
        response = requests.get(link)
        os.makedirs(username, exist_ok=True)

        path = "./"+username+"/"+username+str(count)+"_"+str(data).replace(":","_")+extension
        print(colored("\n[SUCCESS]: saving in path: " + path, "green"))

        open(path, "wb").write(response.content)
        count += 1
    
    return True

isMoreThanOne = False
users = []

if sys.argv[1] is None or sys.argv[1] == "":
    with open('./users.txt', "r") as f:
        for line in f:
            users.append(line.strip())
    isMoreThanOne = True
    
elif sys.argv[1] == "-f" and sys.argv[2] is not None :
    with open('./'+str(sys.argv[1]), "r") as f:
        for line in f:
            users.append(line.strip())
    isMoreThanOne = True

elif sys.argv[1] == "-l":
    for user in sys.argv[2:]:
        users.append(user.strip())
else:
    username = sys.argv[1]
    result = save_stories_of_user(username)

    if result:
        print(colored("\n[SUCCESS]: stories saved for user: " + username, "green"))
    else:
        print(colored("\n[ERROR]: stories not saved for user: " + username, "red"))

if isMoreThanOne:
    print(colored("\n[INFO]: getting stories for users in file: " + str(sys.argv[1]), "yellow"))
    for username in users :
            result = save_stories_of_user(username)

            if result:
                print(colored("\n[SUCCESS]: stories saved for user: " + username, "green"))
            else:
                print(colored("\n[ERROR]: stories not saved for user: " + username, "red"))
