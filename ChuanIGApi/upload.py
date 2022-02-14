from .Import import *

class Upload:

    def delete_post(self, post_link):
        if post_link.find('/tv/') != -1:
            post_link = post_link.replace('/tv/', '/p/')
        try:
            post_link = post_link.replace(post_link.split('/p/')[1].split('/')[1], '')
        except:
            pass
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
        try:
            data_object = data_script.replace(");</script>", '')
            data_json = json.loads(data_object)
            id_post = data_json["items"][0]["pk"]

            url_post = f"https://www.instagram.com/create/{id_post}/delete/"

            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "0",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "cookie": self.cookie,
                "x-ig-app-id": "936619743392459",
                "x-csrftoken": self.csrf_token,
                "x-ig-www-claim": "hmac.AR1Uxa-i6UDIj_f8kEfjLZnqLaHPhGcIacYYdREg0wvh4wCt",
                "x-instagram-ajax": "dbbaa1312a79",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "198387",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "origin": "https://www.instagram.com",
                "referer": post_link
            }
            response = requests.request("POST", url_post, headers=headers, proxies=self.proxy)

            if response.status_code != 200:
                return response.status_code
        except:
            return 403
        
        return 200

    def upload_post(self, image_path, caption=''):
        micro_time = int(datetime.now().timestamp())

        headers = {
            "content-type": "image / jpg",
            "content-length": "1",
            "X-Entity-Name": f"fb_uploader_{micro_time}",
            "Offset": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "x-entity-length": "1",
            "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080, "upload_media_width": 1080}}',
            "x-csrftoken": self.csrf_token,
            "x-ig-app-id": "1217981644879628",
            "cookie": self.cookie
        }

        upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                        data=open(image_path, "rb"), headers=headers, proxies=self.proxy)

        json_data = json.loads(upload_response.text)
        upload_id = json_data['upload_id']

        if json_data["status"] == "ok":
            url = "https://www.instagram.com/create/configure/"

            payload = 'upload_id=' + upload_id + '&caption=' + caption + '&usertags=&custom_accessibility_caption=&retry_timeout='
            payload = payload.encode('utf-8')
            headers = {
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
                'x-instagram-ajax': 'adb961e446b7-hot',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': self.csrf_token,
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/create/details/',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                'cookie': self.cookie
            }

            response = requests.request("POST", url, headers=headers, data=payload, proxies=self.proxy)
            json_data = json.loads(response.text)

            if json_data["status"] == "ok":
                return 200

        else:
            return 400

    def upload_story(self, image_path):
        micro_time = int(datetime.now().timestamp())

        headers = {
            "content-type": "image / jpg",
            "content-length": "1",
            "X-Entity-Name": f"fb_uploader_{micro_time}",
            "Offset": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "x-entity-length": "1",
            "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080, "upload_media_width": 1080}}',
            "x-csrftoken": self.csrf_token,
            "x-ig-app-id": "1217981644879628",
            "cookie": self.cookie
        }

        upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                        data=open(image_path, "rb"), headers=headers, proxies=self.proxy)

        json_data = json.loads(upload_response.text)
        upload_id = json_data['upload_id']

        if json_data["status"] == "ok":
            url = "https://www.instagram.com/create/configure_to_story/"

            payload = 'upload_id=' + upload_id + '&caption=&usertags=&custom_accessibility_caption=&retry_timeout='
            headers = {
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
                'x-instagram-ajax': 'adb961e446b7-hot',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': self.csrf_token,
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/create/details/',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                'cookie': self.cookie
            }

            response = requests.request("POST", url, headers=headers, data=payload, proxies=self.proxy)
            json_data = json.loads(response.text)

            if json_data["status"] == "ok":
                return 200

        else:
            return 400