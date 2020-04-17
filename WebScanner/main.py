from utils import *

def gather_info(name, full_url):
    tld = top_level_domain(full_url)
    print(tld)
    whois_data = get_whois(tld)
    ip_address = get_ip(tld)
    print(ip_address)

    #saving info into specific folder
    projec_dir = 'ROOT_FOLDER' + '/' + name
    make_dir(projec_dir)
    save_data(projec_dir + '/tld.txt' , tld)
    save_data(projec_dir + '/whois_info.txt', whois_data)
    save_data(projec_dir + '/ipaddress.txt', ip_address)

if __name__ == "__main__":
    gather_info('Facebook', 'https://www.facebook.com')