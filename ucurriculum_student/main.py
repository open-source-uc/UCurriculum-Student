import requests
from time import sleep
from bs4 import BeautifulSoup
from uc_sso import get_ticket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class Student:

    def __init__(self, name, password):
        """
        First Step:
        Given the name and password, access the URL of "Seguimiento Curricular UC" 
        and submit the form.
        """
        # Do not open a browser when choosing the webdriver
        options = Options()
        options.add_argument("--headless")

        # Choose the webdriver
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        # Get tickets from the SSO UC. (The get_ticket function handles the error of invalid credentials)
        ticket = get_ticket(name, password, "https://seguimientocurricular.uc.cl/")

        # Access the URL
        self.driver.get(ticket.service_url)

        # Find the drop-down element by id and select the value of the option
        dropdown = Select(self.driver.find_element(By.ID, "j_idt49:_t52"))
        dropdown.select_by_index(0)

        # Submit the drop-down form
        self.driver.find_element(By.ID, "j_idt49:_t55").click()

        """
        Second Step:
        Obtain the HTML from the page solving the problem of the nested Javascript
        """

        # Wait for the page to load and execute the scripts in order to obtain the HTML
        sleep(5)
        html_text = self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

        # Read the html text
        self.soup = BeautifulSoup(html_text, "lxml")

    def actual_courses(self):
        """
        Return the actual courses that the student is coursing.
        This function will return a dictionary specifing the section that the student is;
        in the form of {COURSE: SECTION}
        """

        # Initialization of variables
        actual_courses = {}
        i = 0

        # Loop until we can't find any more courses
        while True:
            
            # Find the raw course
            raw_course = self.soup.find("span", id=f"j_idt49:_t253:{i}:_t257")

            # Break statement
            if raw_course is None:
                break

            # Find the raw section of the raw course
            raw_section = self.soup.find("span", id=f"j_idt49:_t253:{i}:_t277")
            
            course = raw_course.text
            section = raw_section.text
            actual_courses[course] = section
            i += 1

        return actual_courses