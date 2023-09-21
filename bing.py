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
