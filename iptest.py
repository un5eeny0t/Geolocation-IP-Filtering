import requests
import csv
import time

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['country'], data['as']
        else:
            return None, None
    else:
        return None, None

def save_to_file(ip, country, asn, filename='ip_info.csv'):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip, country, asn])

def main():
    with open('ip.txt', 'r') as file:
        ip_list = [line.strip() for line in file.readlines()]

    for ip in ip_list:
        country, asn = get_ip_info(ip)
        if country and asn:
            save_to_file(ip, country, asn)
        else:
            save_to_file(ip, "N/A", "N/A")

        # Introduce a delay of 1 second between each request
        time.sleep(0.1)

if __name__ == "__main__":
    main()
