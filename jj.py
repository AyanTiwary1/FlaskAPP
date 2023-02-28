from flask import Flask ,render_template
from selenium  import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
app = Flask(__name__)
headings = ("Title", " url ", " ThumbNail "," Views "," Time of Posting ")

@app.route("/", methods = ['GET'])
def homepage():
    driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/@PW-Foundation/videos")
    content = driver.page_source.encode('utf-8').strip()
    soup = bs(content, 'lxml')
    #EXTRACTING TITLE AND URL
    video_title = soup.findAll('a' , id='video-title-link')
    video_url = soup.findAll('a' , id='video-title-link')
    url_list=[]
    for k in video_url[:5]:
        
        dd=k.get('href')
        url_list.append(dd)
    # EXTRACTING THUMBNAIL    
    thumbnail = soup.select('img.yt-img-shadow')
    thumb = []
    
    for pic in thumbnail:
        pp = pic.get('src')
        thumb.append(pp)
    # EXTRACTING VIEW
    views = soup.findAll('span', class_ = "inline-metadata-item style-scope ytd-video-meta-block")
    kk=[]
    for total_view in views[0::2]:
        kk.append(total_view.text)

    # EXTRACTING TIME
    when = soup.findAll('span', class_ = "inline-metadata-item style-scope ytd-video-meta-block")
    din=[]
    for day in when[1::4]:
        din.append(day.text)



        

    
        
    
    


    return render_template("table.html",headings=headings, video_title=video_title, url_list=url_list, thumb=thumb, kk=kk, din=din)

if __name__=="__main__":
    app.run(debug=True)