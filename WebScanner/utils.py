import os
from tld import get_fld

#function to make a directory for saving different host
def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


#function to save information
def save_data(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


#function to convert url into top level domain
def top_level_domain(url):
    tld = get_fld(url)
    return tld
    
#url :- https://www.youtube.com/
#o/p :- youtube.com

# print(top_level_domain('https://www.amazon.com/'))

#function for whois information #url is toplevel domain
def get_whois(url):
    action = "whois " + url
    process = os.popen(action)
    result = process.read()
    return result
# print(get_whois('Facebook.com'))

def get_ip(url):
    action = "host " + url
    process = os.popen(action)
    result = str(process.read())
    pointer = result.find('has address') + 12
    # pointer1 = result.find('has IPv6 address') + 17
    return result[pointer:].splitlines()[0]
# print(get_ip('facebook.com'))
