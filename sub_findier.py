import requests

domain = input("[+]Enter Domain To scan :")

file = open("< ----World list path---- >")
content = file.read()

subdomains = content.splitlines()

subdomainsmain = []

for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] discovered Subdomains : " + url)
        subdomainsmain.append(url)
    
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in subdomainsmain:
        print(subdomain, file=f)
