from urllib.parse import urlparse, parse_qs
import re
import requests

class RecaptchaV3:
    def __init__(self) -> None:
        self.anchor_url = "https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly9vcGVuLnNwb3RpZnkuY29tOjQ0Mw..&hl=tr&v=_ZpyzC9NQw3gYt1GHTrnprhx&size=invisible&cb=fg6ln5l9yeeb"
        self.reload_url = "https://www.google.com/recaptcha/enterprise/reload?k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        }

    def recaptchav3_bypass(self) -> str:
        url_var = parse_qs(urlparse(self.anchor_url).query)

        r = requests.get(self.anchor_url, headers=self.headers)
        anchor_token = re.search(r'type="hidden" id="recaptcha-token" value="([^"]+)"', r.text).group(1)

        value1 = url_var['v'][0]
        value2 = url_var['k'][0]
        value3 = url_var['co'][0]

        data = f"v={value1}&reason=q&c={anchor_token}&k={value2}&co={value3}&hl=en&size=invisible"

        self.headers.update({
            "Referer": r.url,
            "Content-Type": "application/x-www-form-urlencoded"
        })

        r = requests.post(self.reload_url, headers=self.headers, data=data)
        return r.text.split('["rresp","')[1].split('"')[0]