import requests
from bs4 import BeautifulSoup
import os
'''
###################################################################################
                                                                          #########
                      "ALL INFORMATION SHALL FOREVER REMAIN FREE"         #########
                          -//GHOST                                        #########
                                                                          #########
                                  aghostlyghoul@pm.me                     #########
                                  -------------------                     #########
###################################################################################
'''


def scrape_website(url, level, log_file, file_ext_log, backup_log):
    if level == 0:
        return

    # GIVE IT HEADDDD
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)'}
    headers = {'Accept': '*/*'}
    #headers = {'Accept-Encoding': 'utf-8'}
    #headers = {'Accept-Language': 'en-UK'}
    #headers = {'compression': 'chunked, gzip, deflate, chunked'}
    #headers = {'Cache-Control': 'no-transform'}
    response = requests.get(url, headers=headers)

    # IM OK..I SWEAR IM 200....
    if response.status_code == 200:
        # IT NO DUMB YOU DUMBBBBB
        soup = BeautifulSoup(response.content, 'html.parser')

        # LOG SHIT
        log_file.write(url + '\n')

        # LINK SPECSSSSSS
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = link['href']
            if next_url.startswith('http'):
                # SHIT YOUR LOOKING FORRRRRRR
                if next_url.split('.')[-1] in ['html', 'htm', 'css', 'js', 'txt', 'xml', 'xss', 'doc', 'py', 'exe', 'apk', 'pdf', 'pwd', 'jpg', 'png', 'gif', 'gz', 'zip', 'iso', 'jpeg', 'torrent', 'sh', 'zsh', 'bin', 'list', 'rc', 'conf', 'git', 'file', 'flv', 'mp4', 'mp3', 'mpeg', 'mpg', 'deb', 'mov', 'flv', 'wav', 'ogv', 'log', 'info', '7gz', 'go', 'CMD', 'cmd', 'com', 'org', 'us', 'rs', 'mx', 'gov', 'psd', 'x', 'bmg', 'ini', 'pcap', 'pcapng', 'md', 'img']:
                    file_ext_log.write(next_url + '\n')
                # RECURSE TO HELLLLLLL
                scrape_website(next_url, level-1, log_file, file_ext_log, backup_log)

        # BULK RAW CODE BACKUPPPPPPPP
        backup_log.write(response.content.decode('utf-8') + '\n')

# LOGZZZZZ
log_file = open('url_log1.txt', 'w')
file_ext_log = open('file_ext_log1.txt', 'w')
backup_log = open('backup_log1.txt', 'w')

# TARGET SPECIFICATIONNNNN
scrape_website('FULL URL GOES HERE', 50, log_file, file_ext_log, backup_log)

# KILL THE LOGZZZZZ
log_file.close()
file_ext_log.close()
backup_log.close()
#
#
#
