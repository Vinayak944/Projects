from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://in.bookmyshow.com/explore/home/alappuzha')
driver.implicitly_wait(5)
my_element = driver.find_element(By.ID,"https://in.bookmyshow.com/alappuzha/movies/antony-2023/ET00376678-0")
my_element.click()
driver.implicitly_wait(5)
time.sleep(5)
# my_element = driver.find_element(By.ID,"https://in.bookmyshow.com/alappuzha/movies/antony-2023/ET00376678-0")

# <a href="https://in.bookmyshow.com/alappuzha/movies/antony-2023/ET00376678" 
# id="https://in.bookmyshow.com/alappuzha/movies/antony-2023/ET00376678-0" 
# class="commonStyles__LinkWrapper-sc-133848s-11 style__CardContainer-sc-lnhrs7-5 kcFNYT">
# <div class="style__VerticalCardContainer-sc-dv5ht7-0 crxcDb">
# <div class="commonStyles__VerticalFlexBox-sc-133848s-2 style__TagsWrapper-sc-5afure-0 byaznB"></div>
# <div width="100%" height="100%" data-content="Antony (2023)" class="sc-133848s-2 sc-1t5vwh0-0 gBMTdX">
# <div class="commonStyles__VerticalFlexBox-sc-133848s-2 style__ImageWrapper-sc-1t5vwh0-1 dXHMBz">
# <img src="https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OC43LzEwICA3LjZLIFZvdGVz,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00376678-uvzdrtxnuh-portrait.jpg" alt="Antony (2023)" width="100%" height="100%"></div></div><div style="margin:4px 0px 0px 0px;padding:4px 0px 0px 0px" class="commonStyles__HorizontalFlexBox-sc-133848s-3 dVLjTu"><div class="commonStyles__VerticalFlexBox-sc-133848s-2 commonStyles__CardTextBox-sc-133848s-12 cIKQwG"><div class="style__StyledText-sc-7o7nez-0 eJQlCo">Antony (2023)</div></div><div class="commonStyles__VerticalFlexBox-sc-133848s-2 commonStyles__CardTextBox-sc-133848s-12 cIKQwG"><div class="style__StyledText-sc-7o7nez-0 fIlqSN">Action/Drama</div></div><h3 class="commonStyles__SeoHeaderTag-sc-133848s-16 iWuYyu">Antony (2023)</h3></div></div></a>