def find_description(soup):
    try:
        description = soup.find('div', { "class" : "C4VMK"})[0].find('span').text
        return description
    except:
        pass
    try:
        description = soup.find('div', { "class" : "C4VMK"}).find('span')
        return description
    except:
        return "Error"

def scrape_post(soup, profile, url):
    try:
        likes = soup.find('div', {'class' : 'Nm9Fw'}).find('span').text
    except:
        likes = None

    description = find_description(soup)

    try:
        img_src = soup.find('img')[0].attrs['src']
    except:
        img_src = None
    
    try:
        date = soup.find('time')[0].attrs['datetime']
    except:
        date = None
    
    try:
        comments = len(soup.find('ul', {'class' : 'XQXOT'}).find('span')) - 1
    except:
        comments = None


    return {
        **profile,
        'likes' : likes,
        'comments' : comments,
        "description" : description,
        'date' : date,
        "img_src" : img_src,
        "post_url" : url
    }
 