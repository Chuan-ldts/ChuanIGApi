from .Import import *

class Comment:

    def comment(self, post_link, comment_text):
        if post_link.find('/tv/') != -1:
            post_link = post_link.replace('/tv/', '/p/')
        try:
            post_link = post_link.replace(post_link.split('/p/')[1].split('/')[1], '')
        except:
            pass
        try:
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

            url_post = f"https://www.instagram.com/web/comments/{id_post}/add/"

            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "39",
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
                "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                "x-instagram-ajax": "d3d3aea32e75",
                "x-requested-with": "XMLHttpRequest"
            }

            response = requests.request("POST", url_post, headers=headers, data=f"comment_text={comment_text}&replied_to_comment_id=".encode('utf-8'), proxies=self.proxy)
                
            if response.status_code != 200:
                return response.status_code
        except:
            return 403

        return 200

    def comment_recent(self, username, comment_text):  
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
            return self.comment('https://www.instagram.com/p/'+shortcode+'/', comment_text)
        except IndexError:
            return 404
        except KeyError:
            return 404