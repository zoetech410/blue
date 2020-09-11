import whois, socket, requests, os
from ip2geotools.databases.noncommercial import DbIpCity

def check_ip():
    try:
        socket.gethostbyname(url)
        return 1
    except socket.error:
        return 0

while True:
    url = input("Type website without https:// Example: google.com ==>")
    if url == "":
        pass
    elif int(check_ip()) == 0:
        pass
    else:
        break

def your_ip():
    s = socket.gethostbyname(url)
    print("*** WEBSITE'S IP ADDRESS ***\n")
    print(s,"\n")

def ip_list():
    s = socket.gethostbyname_ex(url) 
    print("*** LIST OF IP FOR YOUR DOMAIN ***\n")
    print(s,"\n")
    
def ip_lookup():
    try:
        domain = whois.whois(url)
        print("*** IP LOOKUP ***\n")
        print(domain.text,"\n")
    except:
        print("IP LOOKUP NOT FOUND")
    
def website_header():
    try:
        print("*** WEBSITE HEADER ***\n")
        x = requests.head("https://"+ url)
        print(x.headers,"\n")
    except:
        print("COULD NOT GET THE WEBSITE'S HEADER")
    
def geo_tool():
    try:
        print("*** GEOLOCATION INFORMATION ***\n")
        s = socket.gethostbyname(url)
        response = DbIpCity.get(s, api_key='free')
        print(response,"\n")
    except:
        print("GEOLOCATION TOOL IS NOT WORKING")

def port_scan():
    ip = socket.gethostbyname(url)
    print("*** PORT SCANNER ***\n")
       
    for port in range(7, 500):
        try:
            s = socket.socket()
            s.settimeout(1)  
            conn = s.connect_ex((ip,port))

            if(conn == 0):
                print ("[+] PORT",port,"IS OPEN",socket.getservbyport(port,"tcp"))
            # else:
                # print("PORT",port,"IS CLOSED")
            s.close()
        except:
            pass
            
def display():
    color = lambda: os.system('color A')
    color()
    your_ip()   
    ip_list()
    ip_lookup()
    website_header()
    geo_tool()
    #port_scan() # port scanner works, but it's better to use other tool like nmap.
    #this function is very slow, and it will skip some open port to stop the script from craching
    
display()