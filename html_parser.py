from bs4 import BeautifulSoup

'''
Clean HTML
! pip install lxml
'''
def clean_html(text):
    return BeautifulSoup(raw_html, "lxml").text

