from .Import import *

class Follow:

    def already_followed(self, username):
        resp = self.session.get('https://www.instagram.com/'+username+'/', proxies=self.proxy)
        time.sleep(1)
        soup = BeautifulSoup(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        try:
            data_script = str(scripts[4])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        except:
            data_script = str(scripts[3])
            time.sleep(1)
            data_script = data_script.replace(
                '''<script type="text/javascript">window._sharedData = ''', '')
            data_object = data_script.replace(";</script>", '')
            data_json = json.loads(data_object)
        followed = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['followed_by_viewer']
        return bool(followed)

    def follow(self, username):
        try:
            if self.already_followed(username) == False:
                resp = self.session.get('https://www.instagram.com/'+username+'/', proxies=self.proxy)
                time.sleep(1)
                soup = BeautifulSoup(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                try:
                    data_script = str(scripts[4])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                except:
                    data_script = str(scripts[3])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                id_page = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['id']

                url_page = f"https://www.instagram.com/web/friendships/{id_page}/follow/"

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/{username}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                response = requests.request("POST", url_page, headers=headers, proxies=self.proxy)
                if response.status_code == 200:
                    return 200
                else:
                    return response.status_code
            else:
                return 208
                
        except KeyError:
            return 404

    def unfollow(self, username):
        try:
            if self.already_followed(username) == True:
                resp = self.session.get('https://www.instagram.com/'+username+'/', proxies=self.proxy)
                time.sleep(1)
                soup = BeautifulSoup(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                try:
                    data_script = str(scripts[4])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                except:
                    data_script = str(scripts[3])
                    time.sleep(1)
                    data_script = data_script.replace(
                        '''<script type="text/javascript">window._sharedData = ''', '')
                    data_object = data_script.replace(";</script>", '')
                    data_json = json.loads(data_object)
                id_page = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']['id']

                url_page = f"https://www.instagram.com/web/friendships/{id_page}/unfollow/"

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/{username}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                response = requests.request("POST", url_page, headers=headers, proxies=self.proxy)
                if response.status_code == 200:
                    return 200
                else:
                    return response.status_code
            else:
                return 208
        except KeyError:
            return 404