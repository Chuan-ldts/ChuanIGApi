from .Import import *

class AuthLogin:

    def Login(self, username, password, cookie = True, proxy=None):
        self.username = username
        self.password = password
        self.cookie = cookie
        self.proxy = proxy

        self.path = os.getcwd()

        if self.cookie == False or os.path.exists(self.path+f'//cookie_{self.username}.bot') == False:
            link = 'https://www.instagram.com/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'

            current_time = int(datetime.now().timestamp())
            response = requests.get(link, proxies=self.proxy)
            try:
                csrf = response.cookies['csrftoken']
            except:
                letters = string.ascii_lowercase
                csrf = ''.join(random.choice(letters) for i in range(8))

            payload = {
                'username': self.username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{current_time}:{self.password}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            login_header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            }

            login_response = requests.post(login_url, data=payload, headers=login_header, proxies=self.proxy)
            json_data = json.loads(login_response.text)

            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()
            try:
                self.csrf_token = cookie_jar['csrftoken']
            except:
                self.csrf_token = csrf

            try:
                if json_data["authenticated"]:
                    pass
                else:
                    print(bcolors.FAIL+"[✗] Login Failed!"+bcolors.ENDC, login_response.text)
                    quit()
            except KeyError:
                try:
                    if json_data["two_factor_required"]:
                        self.ig_nrcb = cookie_jar['ig_nrcb']
                        self.ig_did = cookie_jar['ig_did']
                        self.mid = cookie_jar['mid']

                        otp = input(bcolors.OKBLUE+'[!] Two Factor Auth. Detected! Enter Code Here: '+bcolors.ENDC)
                        twofactor_url = 'https://www.instagram.com/accounts/login/ajax/two_factor/'
                        twofactor_payload = {
                            'username': self.username,
                            'verificationCode': otp,
                            'identifier': json_data["two_factor_info"]["two_factor_identifier"],
                            'queryParams': {}
                        }

                        twofactor_header = {
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-US,en;q=0.9",
                            "content-type": "application/x-www-form-urlencoded",
                            "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                            "origin": "https://www.instagram.com",
                            "referer": "https://www.instagram.com/accounts/login/two_factor?next=%2F",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                            "x-csrftoken": self.csrf_token,
                            "x-ig-app-id": "936619743392459",
                            "x-ig-www-claim": "0",
                            "x-instagram-ajax": "00c4537694a4",
                            "x-requested-with": "XMLHttpRequest"
                        }

                        login_response = requests.post(twofactor_url, data=twofactor_payload, headers=twofactor_header, proxies=self.proxy)
                        try:
                            if login_response.headers['Set-Cookie'] != 0:
                                pass
                        except:
                            try:
                                if json_data["message"]=="checkpoint_required":
                                    self.ig_nrcb = cookie_jar['ig_nrcb']
                                    self.ig_did = cookie_jar['ig_did']
                                    self.mid = cookie_jar['mid']
                                    url='https://www.instagram.com'+json_data['checkpoint_url']
                                    header = {
                                        "accept": "*/*",
                                        "accept-encoding": "gzip, deflate, br",
                                        "accept-language": "en-US,en;q=0.9",
                                        "content-type": "application/x-www-form-urlencoded",
                                        "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                                        "origin": "https://www.instagram.com",
                                        "referer": 'https://instagram.com'+json_data['checkpoint_url'],
                                        "sec-fetch-dest": "empty",
                                        "sec-fetch-mode": "cors",
                                        "sec-fetch-site": "same-origin",
                                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                                        "x-csrftoken": self.csrf_token,
                                        "x-ig-app-id": "936619743392459",
                                        "x-ig-www-claim": "0",
                                        "x-instagram-ajax": "e8e20d8ba618",
                                        "x-requested-with": "XMLHttpRequest"
                                    }
                                    code=input(bcolors.OKBLUE+json.loads(requests.post(url, headers=header, data={'choice': '1'}).text, proxies=self.proxy)['extraData']['content'][1]['text']+' > '+bcolors.ENDC)
                                    if json.loads(requests.post(url, headers=header, data={'security_code': code}).text, proxies=self.proxy)['type']=='CHALLENGE_REDIRECTION':
                                        login_response = requests.post(login_url, data=payload, headers=login_header, proxies=self.proxy)
                                    else:
                                        print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                        quit()
                            except:
                                print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                quit()

                except KeyError:
                    try:
                        if json_data["message"]=="checkpoint_required":
                            self.ig_nrcb = cookie_jar['ig_nrcb']
                            self.ig_did = cookie_jar['ig_did']
                            self.mid = cookie_jar['mid']
                            url='https://www.instagram.com'+json_data['checkpoint_url']
                            header = {
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                "accept-language": "en-US,en;q=0.9",
                                "content-type": "application/x-www-form-urlencoded",
                                "cookie": 'ig_did='+self.ig_did+'; ig_nrcb='+self.ig_nrcb+'; csrftoken='+self.csrf_token+'; mid='+self.mid,
                                "origin": "https://www.instagram.com",
                                "referer": 'https://instagram.com'+json_data['checkpoint_url'],
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                                "x-csrftoken": self.csrf_token,
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "0",
                                "x-instagram-ajax": "e8e20d8ba618",
                                "x-requested-with": "XMLHttpRequest"
                            }
                            code=input(bcolors.OKBLUE+json.loads(requests.post(url, headers=header, data={'choice': '1'}).text, proxies=self.proxy)['extraData']['content'][1]['text']+' > '+bcolors.ENDC)
                            if json.loads(requests.post(url, headers=header, data={'security_code': code}).text, proxies=self.proxy)['type']=='CHALLENGE_REDIRECTION':
                                login_response = requests.post(login_url, data=payload, headers=login_header, proxies=self.proxy)
                            else:
                                print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                                quit()
                    except:
                        print(bcolors.FAIL+'[✗] Login Failed!'+bcolors.ENDC)
                        quit()

            self.sessionid = login_response.headers['Set-Cookie'].split('sessionid=')[1].split(';')[0]                
            self.userId =   login_response.headers['Set-Cookie'].split('ds_user_id=')[1].split(';')[0]              
            self.cookie = "sessionid=" + self.sessionid + "; csrftoken=" + self.csrf_token + "; ds_user_id=" + self.userId + ";"
            create_cookie = open(self.path+f'//cookie_{self.username}.bot', 'w+', encoding='utf-8')
            create_cookie.write(self.cookie)
            create_cookie.close()
            self.session = requests.session()
            cookie_obj = requests.cookies.create_cookie(
                    name='sessionid', secure=True, value=self.sessionid)
            self.session.cookies.set_cookie(cookie_obj)

        elif os.path.exists(self.path+f'//cookie_{self.username}.bot'):
            try:
                read_cookie = open(self.path+f'//cookie_{self.username}.bot', 'r', encoding='utf-8')
                self.cookie = read_cookie.read()
                read_cookie.close()
                homelink = 'https://www.instagram.com/op/'
                self.session = requests.session()
                self.sessionid = self.cookie.split('=')[1].split(';')[0]
                self.csrf_token = self.cookie.split('=')[2].split(';')[0]
                cookie_obj = requests.cookies.create_cookie(
                    name='sessionid', secure=True, value=self.sessionid)
                self.session.cookies.set_cookie(cookie_obj)
                login_response = self.session.get(homelink, proxies=self.proxy)
                time.sleep(1)
                soup = BeautifulSoup(login_response.text, 'html.parser')
                soup.find("strong", {"class": "-cx-PRIVATE-NavBar__username -cx-PRIVATE-NavBar__username__"}).get_text()
            except AttributeError:
                print(bcolors.FAIL+"[✗] Login Failed! Cookie file is corupted!"+bcolors.ENDC)
                os.remove(self.path+f'//cookie_{self.username}.bot')
                print(bcolors.WARNING+"[-] Deleted Corupted Cookie File! Try Again!"+bcolors.ENDC)
                quit()