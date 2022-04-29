from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Do not open a browser when choosing the webdriver
options = Options()
options.add_argument("--headless")

# Choose the webdriver and enter the BuscaCursos web
DRIVER = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
DRIVER.get("https://buscacursos.uc.cl/")

def CourseSchedule(nrc_course):

    # Find the NRC section of the code
    DRIVER.find_element(By.NAME, "cxml_nrc").send_keys(nrc_course)

    # Find the button to upload the information
    DRIVER.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/div/div/div[2]/div[1]/div/div[4]/div/div[2]/div/form/input[1]").click()

    # Search for the schedule information
    raw_information = DRIVER.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/div/div/div[3]/table/tbody/tr[4]/td[17]/table")

    # Transform the raw information
    string = raw_information.text
    # Initialization of variables
    start = 0
    course_schedule = {}
    type = False

    # Loop in order to extract the schedule from the string
    for i in range(len(string)):
        
        # Check for schedule
        if string[i] == ":":
            type = True
            finish = i+1
            schedule = string[start:finish+1]

        # Check for whitespace
        elif string[i] == " " or string[i] == "\n":
            
            # If the schedule has been already read, initialize the reading of the type of schedule
            if type is True:
                init = True
                type = False
                start = i+1

            # Check if we are at the end of the type of schedule in order to append
            elif init is True:
                init = False
                type_of_schedule = string[start:i]
                course_schedule[type_of_schedule] = schedule

            else:
                start = i+1

    # Return statement
    return course_schedule