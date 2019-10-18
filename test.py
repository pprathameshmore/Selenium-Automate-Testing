from selenium import webdriver
from selenium.webdriver.common.by import By

from faker import Faker

import glob
import os
import time
import sys

URL = "http://localhost/timeline-app/"

images = glob.glob("images/*.jpg")

if sys.argv[1].strip() != "":
    TEST_FOR = len(images)
else:
    TEST_FOR = int(sys.argv[1].strip())
    images = images[0:int(sys.argv[1].strip()) + 1]

with webdriver.Chrome() as dv:

    dv.get(URL)

    dv.set_window_size(500, 500)
    dv.maximize_window()

    dv.implicitly_wait(10)

    emails = []
    descriptions = []

    fake = Faker()

    for _ in range(TEST_FOR):
        emails.append(fake.email())
        descriptions.append(fake.sentence())
        
    for i, email, description, image in zip(range(len(images)), emails, descriptions, images):
        email_elem = dv.find_element(By.NAME, 'title')
        email_elem.send_keys(email)

        desc_elem = dv.find_element(By.NAME, 'description')
        desc_elem.send_keys(description)

        image_elem = dv.find_element(By.NAME, 'image')
        image_elem.send_keys(os.getcwd() + "/" + image)

        submit_btn = dv.find_element(By.ID, 'btnSumbit')
        submit_btn.click()

        print(f"{i} done!")

        time.sleep(0.5) # remove if you feel it's tooooooooooooooooooooooooooooooooo slows


    print("All Done!")

