try:
    import time,requests,os
    from instabot import Bot
    from colorama import Fore
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install instabot')
    os.system('pip install colorama')
    os.system('pip install tqdm')
    os.system('pip install requests_toolbelt')
    print('\n[+] Done')
print("""
       Comments
___ _   _     _        
|_ _| \ | |___| |_ __ _ 
 | ||  \| / __| __/ _` |
 | || |\  \__ \ || (_| |
|___|_| \_|___/\__\__,_|                    
""")
print("BY BLACK MIROR")
print("=====================================")
done=0
b=Bot
error=0
user = input("USER : ")
pess = input("PASS : ")
tx = input("YOUR TXT : ")
post = input("POST URL : ")
print("=====================================")
idd=b.get_media_id_from_link(self='',link=post)
slp = int(7.1)
urLG = "https://www.instagram.com/accounts/login/ajax/"
headLG = {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': '*/*',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
    'X-Instagram-AJAX': '1d6caaf37cd2',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '437806',
    'X-IG-WWW-Claim': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '347',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/login/',
    'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
    'TE': 'Trailers'}
datLG = {
    'username': user,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}',
    'queryParams': "{}",
    'optIntoOneTap': 'false',
    'stopDeletionNonce ': "",
    'trustedDeviceRecords': "{}"}
go = requests.post(urLG, headers=headLG, data=datLG)
if ("userId") in go.text:
    sis = go.cookies['sessionid']
    urCOm = f'https://www.instagram.com/web/comments/{idd}/add/'
    hedCOM = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '44',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid=' + sis,
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/p/CMmx4KOpnx6/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
    'x-instagram-ajax': '753ce878cd6d',
    'x-requested-with': 'XMLHttpRequest'}
    daCOM = {
        'comment_text': tx,
        'replied_to_comment_id': ''}
    while True:
        time.sleep(slp)
        ct = requests.post(urCOm, headers=hedCOM, data=daCOM)
        if '"status":"ok"' in ct.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{idd}]  Text [{tx}]{Fore.RESET}',end='')
            done+=1
        elif 'Please' in ct.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{idd}]  Text [{tx}]{Fore.RESET}',end='')
            error+=1
        elif ("two_factor") in go.text:
            print('\n[⛔️] Binary verification \n')
            break
        elif ("checkpoint_url") in go.text:
            print('\n[⚠️] Account Secure \n')
            break
        else:
            print('\n[✖️] The username or password or post id is wrong! \n')
            break
