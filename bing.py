import requests
import json
import os
import sys
from termcolor import colored

ip = requests.get("https://api.ipify.org").text


def submit_single_url(api_key, site_url, page_url):
    url = f"https://ssl.bing.com/webmaster/api.svc/json/SubmitUrl?apikey={api_key}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"siteUrl": site_url, "url": page_url}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(colored("\nBerhasil Dikirim", "green"))
    else:
        print(colored("Gagal mengirim permintaan.", "red"))


def submit_batch_urls(api_key, site_url, url_list):
    url = f"https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch?apikey={api_key}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"siteUrl": site_url, "urlList": url_list}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(colored("\nBerhasil Dikirim", "green"))
    else:
        print(colored("Gagal mengirim permintaan.", "red"))


def read_api_key():
    try:
        with open("api.txt", "r") as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print("File api.txt tidak ditemukan.")
        sys.exit(1)


def get_quota(api_key, site_url):
    url = f"https://ssl.bing.com/webmaster/api.svc/json/GetUrlSubmissionQuota?siteUrl={site_url}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        quota_data = response.json().get("d")
        daily_quota = quota_data.get("DailyQuota")
        monthly_quota = quota_data.get("MonthlyQuota")
        print(f"Kuota Harian: {daily_quota}")
        print(f"Kuota Bulanan: {monthly_quota}")
    else:
        print(colored("Gagal mendapatkan kuota.", "red"))

def main_menu():
    banner = """
    ██████╗ ██╗███╗   ██╗██████╗ ███████╗██╗  ██╗
    ██╔══██╗██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝
    ██████╔╝██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ 
    ██╔══██╗██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ 
    ██████╔╝██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗
    ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
       """
    print(banner)
    print(colored("Your IP: ", "blue"), colored(ip, "green"))
    print(colored("Author:", "blue"), colored("DomathID", "green"))
    print(colored("Github:", "blue"), colored("https://github.com/DomathID", "green"))
    print("\nMenu Utama:")
    print(colored("[1]", "magenta"), "Submit URL Single")
    print(colored("[2]", "magenta"), "Submit URL dalam Batch")
    print(colored("[3]", "magenta"), "Cek Kuota")
    print(colored("[4]", "magenta"), "Keluar")

    choice = input("Pilih opsi (1/2/3/4): ")
    if choice == "1":
        api_key = read_api_key()
        site_url = input("URL situs: ")
        page_url = input("Page Situs: ")
        submit_single_url(api_key, site_url, page_url)
    elif choice == "2":
        api_key = read_api_key()
        site_url = input("Masukkan URL situs: ")
        url_list = []
        count = 1
        while True:
            url = input(f"Masukkan URL {count} (kosongkan untuk selesai): ")
            if url == "":
                break
            url_list.append(url)
            count += 1
        submit_batch_urls(api_key, site_url, url_list)
    elif choice == "3":
        api_key = read_api_key()
        site_url = input("URL situs: ")
        get_quota(api_key, site_url)
    elif choice == "4":
        print("Keluar dari Tools")
        sys.exit(0)
    else:
        print(colored("Opsi tidak valid. Silakan pilih opsi yang valid.", "yellow"))
main_menu()
