'''
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    url = url[url.index('//')+2:] if '//' in url else url 
    url = url[url.index('www.')+4:] if 'www.' in url else url 
    url = url[:url.index('.')] 
    return url
