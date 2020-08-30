def scrape_post(soup, profile):
    try:
        likes = soup.find('div', {'class' : 'Nm9Fw'}).find('span').text
    except:
        likes = 'VIDEO'
    
    date = soup.find('time')[0].attrs['datetime']
    comments = len(soup.find('ul', {'class' : 'XQXOT'}).find('span')) - 1
    
    return {
        **profile,
        'likes' : likes,
        'date' : date,
        'comments' : comments
    }
