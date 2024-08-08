# ProxyToolKit
## All New way to check and Scrape Proxy in Detail

***ProxyToolKit is a Python script that Scrape Proxy from Multiple websites and return proxy according to users wish<br>
also check Proxy and retun a dict as responce contain [ Porotocol type, Latency, Country, Checked Time, Anonimity ]<br>***
<br>
<br>

***ProxyToolKit Contain 2 Classes:*** ScrapeProxy, CheckProxy<br>
### ***ScrapeProxy*** Class
This Class used to Scape Proxyies and retun as a list
###### Usage:
```
proxy = ScrapeProxy().scrape(type_)
Print(proxy)
"## responce"
"[x.x.x.x:port,......]"

```
***Types : ['all','http','https','socks4','socks5']<br>
all: all protocol like 'http','https','socks4','socks5'<br>
http: retune Http Proxys<br>
https: retune Https Proxys<br>
socks4: retune Socks4 Proxys<br>s
socks5: retune Socks5 Proxys<br>***

### ***CheckProxy*** Class
This Class used to Scape Proxyies and retun as a dict:
sampel: <br>
{<br>
    'status': status,<br>
    'proxy': proxy,<br>
    'protocols':protocols,<br>
    'country': country,<br>
    'anonymity': anonymity,<br>
    'latency': timeout,<br>
    'last_checked': Checked time,<br>
    remote_address: Remote address<br>
}<br>
###### Usage:
```
proxy = ScrapeProxy().scrape(type_)
Print(proxy)
"## responce"
"[x.x.x.x:port,......]"
result =CheckProxy().check_proxy(proxy:str, check_country=True, check_address=True)
print(result)
### responce:
{
    'status': status,
    'proxy': proxy,
    'protocols':protocols,
    'country': country,
    'anonymity': anonymity,
    'latency': timeout,
    'last_checked': Checked time,
}
```
***Note: cheking proxies one proxy at a time:***<br>
****proxy:str = Proxy eg: 'x.x.x.x:0000' <br>
check_country=True; For check which contry the proxy is; By default it set as "True"<br> 
check_address=True; For get remote remote address; By default it set as "True"<br>***



### ***Up-Coming Update***:
***[1] Inbuild looping<br>[2] Inbuild Database For Save Checked Proxies<br>[3] More Proxys responce<br>[3] Advanced Details about checked Proxies<br>[4] Stablized multi threading for faster checking*** 


#### Donate
USDT (ERC-20)
```0xc6fe979f191e251b92f71f35353ae658bff68b80```<br>
Ethereum (ERC-20)
```0xc6fe979f191e251b92f71f35353ae658bff68b80```<br>
Bitcoin (BTC)
```1N4dMtYgQCdRFSCcgKXSECxiwndeoqZZ5r```<br>
<br>
<br>
support us on:<br>
<a href="https://t.me/https://t.me/CodingWithDevil_yt"><img src="https://img.shields.io/badge/telegram-D14836?color=2CA5E0&style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://www.instagram.com/mr_torque_411_/"><img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://www.youtube.com/c/codingwithdevil"><img src="https://img.shields.io/youtube/channel/subscribers/UCnKlznTEohj_PCw9cuxy8Zg?style=social"></a>