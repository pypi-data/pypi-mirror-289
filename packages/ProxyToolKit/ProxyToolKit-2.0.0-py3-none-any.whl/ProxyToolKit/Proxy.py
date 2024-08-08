import requests as rqs
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
from .Exceptions import *
import random
from ProxyToolKit.agents import user_agents
import re, time
from datetime import datetime

class ScrapeProxy():
    def __init__(self):
        self.proxy_types = ['all','http','https','socks4','socks5']
        self.proxyscrape = "https://api.proxyscrape.com/?request=getproxies&proxytype={}&timeout=all&country=all"
        self.proxyscrape_v2 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol={}&timeout=all&country=all"
        self.proxy_list_download = "https://www.proxy-list.download/api/v1/get?type={}&anon=elite"
        self.session = rqs.Session()
        self.session.headers.update({("User-Agent", random.choice(user_agents))})


    def __proxyscrape(self,url):
        proxys = []
        response = self.session.get(url)
        p = response.text
        p = str(p).replace('\r','')
        p = p.split('\n')
        for proxy in p :
            if proxy not in proxy:
                proxys.append(proxy.replace('\n',''))
        return proxys
        
    def __proxyscrape_v3(self,type_):
        proxy_data = []
        res = rqs.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
        if res.ok :
            res = str(res.text).replace('\r','')
            res  = res.split('\n')
            for item in res:
                item = item.replace('//','').replace('\r','').replace('\n','')
                item = item.split(':')
                # print(item)
                if len(item) == 3:
                    proxy_dat = f"{item[1]}:{item[2]}"
                    if type_ == item[0]:
                        proxy_data.append(proxy_dat)
                    elif type_ == 'https' and item[0] == 'http':
                        proxy_data.append(proxy_dat)

                else:
                    pass
        
        return proxy_data

    def __us_proxy(self):
        proxys = []
        page = self.session.get("http://us-proxy.org")
        soup = BeautifulSoup(page.text, "html.parser")
        proxies = set()
        table = soup.find("table", attrs={"class": "table table-striped table-bordered"})
        for row in table.findAll("tr"):
            count = 0
            proxy = ""
            for cell in row.findAll("td"):
                if count == 1:
                    proxy += ":" + cell.text.replace("&nbsp;", "")
                    proxies.add(proxy)
                    break
                proxy += cell.text.replace("&nbsp;", "")
                count += 1
                
        for line in proxies:
            proxys.append(line)

        return proxys

    def __filter(self,proxys:list):
        new_proxy = []
        for proxy in proxys:
            if proxy not in new_proxy:
                new_proxy.append(proxy)

        return new_proxy


    def scrape(self,type_:str):
        type_ = type_.lower()
        if type_ in self.proxy_types:
            if type_ == 'all':
                proxy_types = ['http','https','socks4','socks5']
                p =[]
                for p_type in proxy_types:
                    proxyscrape = self.__proxyscrape(self.proxyscrape.format(p_type))
                    proxyscrape_v2 = self.__proxyscrape(self.proxyscrape_v2.format(p_type))
                    proxy_list_download = self.__proxyscrape(self.proxy_list_download.format(p_type))
                    proxyscrape_v3 = self.__proxyscrape_v3(p_type)
                    p.append(proxyscrape)
                    p.append(proxyscrape_v2)
                    p.append(proxy_list_download)
                    p.append(proxyscrape_v3)
                us_proxy = self.__us_proxy()
                proxy =[]
                for prox in p:
                    proxy+=prox
                proxy+= us_proxy
                filtered_proxy = self.__filter(proxy)
            else:
                proxyscrape = self.__proxyscrape(self.proxyscrape.format(type_))
                proxyscrape_v2 = self.__proxyscrape(self.proxyscrape_v2.format(type_))
                proxy_list_download = self.__proxyscrape(self.proxy_list_download.format(type_))
                proxyscrape_v3 = self.__proxyscrape_v3(type_)
                proxy = proxyscrape+proxyscrape_v2+proxyscrape_v3+proxy_list_download
                filtered_proxy = self.__filter(proxy)

            return filtered_proxy
        else:
            raise ProxyTypeError()


class CheckProxy:
    def __init__(self):
        self.session = rqs.Session()
        
        self.ip = self.get_ip()
        self.proxy_judges = [
            'http://proxyjudge.us/',
            'http://mojeip.net.pl/asdfa/azenv.php'
        ]

    def send_query(self, proxy=None, url=None, user=None, password=None):
        proxies = {}
        if proxy:
            proxies['http'] = proxy
            proxies['https'] = proxy
        
        auth = None
        if user and password:
            auth = HTTPProxyAuth(user, password)

        try:
            start_time = time.time()
            # Perform the request
            response = rqs.get(
                url or random.choice(self.proxy_judges),
                proxies=proxies,
                auth=auth,
                timeout=10  # Timeout in seconds
            )
            end_time = time.time()
            # Check if the HTTP status code is 200
            if response.status_code != 200:
                return False
            
            # Calculate the request timeout in milliseconds (requests does not provide this directly)
            timeout = (end_time - start_time) * 1000  # You can set a fixed value or measure it differently
            timeout = str(timeout).split('.')[0]+'ms'
            # Return the response details
            return {
                'timeout': timeout,
                'response': response.text
            }
        
        except rqs.RequestException:
            # Handle exceptions and errors
            # print(f"Request failed: {e}")
            return False
        
    def get_ip(self):
        session = self.session
        res = session.get('https://api.ipify.org/')
        if res:
            # print()
            return res.text

    def get_country(self, ip):
        response = self.send_query(url=f'https://ip2c.org/{ip}')
        if response and response['response'][0] == '1':
            r = response['response'].split(';')
            return [r[3], r[1]]
        return ['-', '-']
    
    def parse_anonymity(self, r):
        if self.ip in r:
            return 'Transparent'

        privacy_headers = [
            'VIA', 'X-FORWARDED-FOR', 'X-FORWARDED', 
            'FORWARDED-FOR', 'FORWARDED-FOR-IP', 'FORWARDED', 
            'CLIENT-IP', 'PROXY-CONNECTION'
        ]

        if any(header in r for header in privacy_headers):
            return 'Anonymous'

        return 'Elite'
    

    def check_proxy(self,proxy, check_country=True, check_address=True):
        protocols = {}
        timeout = 0

        for protocol in ['http', 'socks4', 'socks5']:
            response = self.send_query(proxy=f"{protocol}://{proxy}")
            if response:
                protocols[protocol] = response
                timeout = response['timeout']

        if not protocols:
            return False
        
        selected_protocol = random.choice(list(protocols.keys()))
        r = protocols[selected_protocol]['response']

        if check_country:
            country = self.get_country(proxy.split(':')[0])
        
        anonymity = self.parse_anonymity(r)
        # timeout = timeout // len(protocols)

        remote_addr = None
        if check_address:
            remote_regex = r'REMOTE_ADDR = (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            match = re.search(remote_regex, r)
            if match:
                remote_addr = match.group(1)

        results = {
            'protocols': list(protocols.keys()),
            'anonymity': anonymity,
            'timeout': timeout,
            'status': 'success'
        }

        if check_country:
            results['country'] = country[0]
            results['country_code'] = country[1]

        if check_address:
            results['remote_address'] = remote_addr

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        res = {
            'status': results.get('status', 'N/A'),
            'proxy': proxy,
            'protocols':results.get('protocols',''),
            'country': results.get('country', 'N/A'),
            'anonymity': results.get('anonymity', 'N/A'),
            'latency': results.get('timeout', 'N/A'),
            'last_checked': formatted_time,
        }


        return res


# CheckProxy().get_ip(proxy='')