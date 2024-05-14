from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soups



 
def search_selenium(search_name, search_limit) :
    # 구글 이미지 검색
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    # 크롬 드라이버 불러오기
    browser = webdriver.Chrome()
    browser.get(search_url)
    # img 파일 불러오기
    image_count = len(browser.find_elements(By.TAG_NAME,"img"))
    
    print("로드된 이미지 개수 : ", image_count)
 
    browser.implicitly_wait(2)
    # 이미지 저장 
    for i in range( search_limit ) :
        image = browser.find_elements(By.TAG_NAME,"img")[2*i+22]
        image.screenshot("./cat_data/" + str(i) + ".png") # 맨 앞에 저장경로 설정.
 
    browser.close()
 
if __name__ == "__main__" :
 
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    
    search_selenium(search_name, search_limit)