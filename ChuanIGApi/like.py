from .Import import *

class LIKE:

    def cekLIKE(self, post):
        self.post = post
        if self.post.find('/tv/') != -1:
            self.post = self.post.replace('/tv/', '/p/')
        try:
            self.post = self.post.replace(self.post.split('/p/')[1].split('/')[1], '')
        except:
            pass
        resp = self.session.get(self.post, proxies=self.proxy)
        time.sleep(1)
        soup = BeautifulSoup(resp.text, 'html.parser')
        scripts = soup.find_all('script')
        script = str(scripts[15])
        time.sleep(1)
        try:
            shortcode = self.post.split('/p/')[1].replace('/', '')
            script = script.replace(
                f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
        except:
            shortcode = self.post.split('/tv/')[1].replace('/', '')
            script = script.replace(
                f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
        objects = script.replace(");</script>", '')
        jsons = json.loads(objects)
        liked = jsons["items"][0]["has_liked"]
        
        return bool(liked)
    
    def like(self, post_link):
        if post_link.find('/tv/') != -1:
            post_link = post_link.replace('/tv/', '/p/')
        try:
            post_link = post_link.replace(post_link.split('/p/')[1].split('/')[1], '')
        except:
            pass
        try:
            if self.cekLIKE(post_link) == False:
                resp = self.session.get(post_link, proxies=self.proxy)
                time.sleep(1)
                soup = BeautifulSoup(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                data_script = str(scripts[15])
                time.sleep(1)
                try:
                    shortcode = post_link.split('/p/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
                except:
                    shortcode = post_link.split('/tv/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
                data_object = data_script.replace(");</script>", '')
                data_json = json.loads(data_object)
                id_post = data_json["items"][0]["pk"]
                
                url_post = f"https://www.instagram.com/web/likes/{id_post}/like/"

                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": post_link,
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFqSx",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }
                response = requests.request("POST", url_post, headers=headers, proxies=self.proxy)

                if response.status_code != 200:
                    return response.status_code
            else:
                return 208
        except:
            return 403

        return 200

    def unlike(self, post_link):
        if post_link.find('/tv/') != -1:
            post_link = post_link.replace('/tv/', '/p/')
        try:
            post_link = post_link.replace(post_link.split('/p/')[1].split('/')[1], '')
        except:
            pass
        try:
            if self.cekLIKE(post_link) == True:
                resp = self.session.get(post_link, proxies=self.proxy)
                time.sleep(1)
                soup = BeautifulSoup(resp.text, 'html.parser')
                scripts = soup.find_all('script')
                data_script = str(scripts[15])
                time.sleep(1)
                try:
                    shortcode = post_link.split('/p/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/p/{shortcode}/',''', '')
                except:
                    shortcode = post_link.split('/tv/')[1].replace('/', '')
                    data_script = data_script.replace(
                        f'''<script type="text/javascript">window.__additionalDataLoaded('/tv/{shortcode}/',''', '')
                data_object = data_script.replace(");</script>", '')
                data_json = json.loads(data_object)
                id_post = data_json["items"][0]["pk"]
                
                url_post = f"https://www.instagram.com/web/likes/{id_post}/unlike/"

                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": self.cookie,
                    "origin": "https://www.instagram.com",
                    "referer": post_link,
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": self.csrf_token,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFqSx",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }
                response = requests.request("POST", url_post, headers=headers, proxies=self.proxy)

                if response.status_code != 200:
                    return response.status_code
            else:
                return 208
                
        except:
            return 403
            
        return 200

    def like_recent(self, username):  
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
        try:
            shortcode = data_json["entry_data"]["ProfilePage"][0]["graphql"]['user']["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]
            return self.like('https://www.instagram.com/p/'+shortcode+'/')
        except IndexError:
            return 404
        except KeyError:
            return 404