'''
This module acquires the information of a student that is searched
using their UCI Net ID, which is unique for every student and returns
a list of that student's information.

# Creator: Guillermo Sanchez
'''

from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_url(uci_id: str) -> urlopen:
    # Builds a custom URL that inserts the student's UCI Net ID and
    # and returns the response of the URL from urlopen
    address = "http://directory.uci.edu/index.php?uid=" + uci_id + \
          "&form_type=plaintext"
    print("Loading...")
    return urlopen(address)


def read_html(opened_url: urlopen) -> None:
    # Takes the resopnse from get_url and reads the html file as a text file
    # and looks for the specific information of the student
    student = list()
    html = BeautifulSoup(opened_url, "html.parser")
    for line in html.body:
        if ":" in line and "E-mail:" not in line and "Delivery" not in line:
            student.append(line)
    return student


def print_student(student: list) -> None:
    # Prints the students information
    for student_info in student:
        student_info = student_info.strip('\n')
        print(student_info)

if __name__ == "__main__":
    while True:
        try:
            uci_id = input("Enter UCI Net ID: ").lower()
            email = "\nE-mail: " + uci_id + "@uci.edu"

            opened_url = get_url(uci_id)
            student = read_html(opened_url)

            student.append(email)
            print()
            print_student(student)

            break
        except TypeError:
            print("ERROR: Invalid UCI Net ID. \nPlease type a valid ID.")
        except URLError:
            print("ERROR: check internet connection." )







