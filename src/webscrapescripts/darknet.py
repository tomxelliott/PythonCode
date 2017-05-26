import socks
import ssl
import requests.cert

s = socks.socksocket()
s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port=9050)
s.connect(('https://nzxj65x32vh2fkhk.onion/all', 443))
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs="requests.cert.where()")

print "Peer cert: ", ss.getpeercert()

ss.write("""GET / HTTP/1.0\r\nHost:https://nzxj65x32vh2fkhk.onion/all\r\n\r\n""")

content = []
while True:
    data = ss.read()
    if not data: break
         content.append(data)


ss.close()
content = "".join(content)
assert "This browser is configured to use Tor" in content








url = "http://nzxj65x32vh2fkhk.onion/all"
proxy = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}

r = requests.get(url, proxies=proxy)
