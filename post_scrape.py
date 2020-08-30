def scrape_post(soup, profile, url):
    try:
        likes = soup.find('div', {'class' : 'Nm9Fw'}).find('span').text
    except:
        likes = 'VIDEO'

    try:
        description = soup.find('div', { "class" : "C4VMK"})[0].find('span').text
    except:
        description = "Error"
    try:
        img_src = soup.find('img')[0].attrs['src']
    except:
        img_src = "Error"
    
    try:
        date = soup.find('time')[0].attrs['datetime']
    except:
        date = "Error"
    # comments = len(soup.find('ul', {'class' : 'XQXOT'}).find('span')) - 1
    return {
        **profile,
        'likes' : likes,
        'date' : date,
        # 'comments' : comments,
        "img_src" : img_src,
        "description" : description,
        "post_url" : url

    }
 