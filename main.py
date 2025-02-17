from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from collections import Counter


driver = webdriver.Chrome()
driver.get(' http://www.imdb.com/chart/top/')

click_button = driver.find_element(by=By.ID , value='list-view-option-detailed')
#<button id="list-view-option-detailed" class="ipc-icon-button ipc-icon-button--base ipc-icon-button--onAccent2" title="Selected:  Detailed view" role="button" tabindex="0" aria-label="Selected:  Detailed view" aria-disabled="false"><svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="ipc-icon ipc-icon--list-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M1.5 13.5c.825 0 1.5-.675 1.5-1.5s-.675-1.5-1.5-1.5S0 11.175 0 12s.675 1.5 1.5 1.5zm0 5c.825 0 1.5-.675 1.5-1.5s-.675-1.5-1.5-1.5S0 16.175 0 17s.675 1.5 1.5 1.5zm0-10C2.325 8.5 3 7.825 3 7s-.675-1.5-1.5-1.5S0 6.175 0 7s.675 1.5 1.5 1.5zm4.857 5h16.286c.746 0 1.357-.675 1.357-1.5s-.61-1.5-1.357-1.5H6.357C5.611 10.5 5 11.175 5 12s.61 1.5 1.357 1.5zm0 5h16.286c.746 0 1.357-.675 1.357-1.5s-.61-1.5-1.357-1.5H6.357C5.611 15.5 5 16.175 5 17s.61 1.5 1.357 1.5zM5 7c0 .825.61 1.5 1.357 1.5h16.286C23.389 8.5 24 7.825 24 7s-.61-1.5-1.357-1.5H6.357C5.611 5.5 5 6.175 5 7zm-3.5 6.5c.825 0 1.5-.675 1.5-1.5s-.675-1.5-1.5-1.5S0 11.175 0 12s.675 1.5 1.5 1.5zm0 5c.825 0 1.5-.675 1.5-1.5s-.675-1.5-1.5-1.5S0 16.175 0 17s.675 1.5 1.5 1.5zm0-10C2.325 8.5 3 7.825 3 7s-.675-1.5-1.5-1.5S0 6.175 0 7s.675 1.5 1.5 1.5zm4.857 5h16.286c.746 0 1.357-.675 1.357-1.5s-.61-1.5-1.357-1.5H6.357C5.611 10.5 5 11.175 5 12s.61 1.5 1.357 1.5zm0 5h16.286c.746 0 1.357-.675 1.357-1.5s-.61-1.5-1.357-1.5H6.357C5.611 15.5 5 16.175 5 17s.61 1.5 1.357 1.5zM5 7c0 .825.61 1.5 1.357 1.5h16.286C23.389 8.5 24 7.825 24 7s-.61-1.5-1.357-1.5H6.357C5.611 5.5 5 6.175 5 7z"></path></svg></button>
click_button.click()

time.sleep(10)
soup = BeautifulSoup(driver.page_source , 'html.parser')
movie_titels = soup.find_all('h3')
movie_titles_text= [titles.text for titles in movie_titels][1:251]
#print(movie_titles_text)
 
movie_plots = soup.find_all('div' , {'class' : 'ipc-html-content ipc-html-content--base sc-74bf520e-0 iiRKKi dli-plot-container'}) 
movie_plots_text= [plots.text.split() for plots in movie_plots]
print(len(movie_titles_text))
print(len(movie_plots_text))
#<div class="ipc-html-content ipc-html-content--base sc-74bf520e-0 iiRKKi dli-plot-container" role="presentation"><div class="ipc-html-content-inner-div">The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.</div></div>
#print(movie_plots_text)
#print('i am here')

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
preprocessed_plots = []
for plot in movie_plots_text:
    preprocessed_plots.append([w for w in plot if not w.lower() in stop_words])




