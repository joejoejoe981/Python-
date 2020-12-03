import requests
import re

# 自定義例外
class PokemonscraperError(Exception):
    def __init__(self,message = None):
        self.message = message
    def __str__(self):
        return self.message

class PokemonScraper:
    def __init__(self):
        response = requests.get(url='http://pokemondb.net/pokedex/national')
        if response.ok:
            self.response = response
            print('成功取得回應')
        else:
            message = '網頁抓取失敗，狀態碼{},原因{}'.format(response.status_code,response.reason)
            raise PokemonscraperError(message)
            # raise 具備 return 的效果
    def get_title(self):
        s = self.response.text
        p = '<title>.*?</title>'
        # m = re.search(p,s)
        # if m:
        #     title = m.group()
        #     return title
        # else:
        #     return None
        a = re.findall(p, s)
        for x in a:
            print(x)

    def get_image_url(self):
        s = self.response.text
        p = 'src=".*?"'
        m = re.search(p,s)
        if m:
            image_url = m.group()
            return image_url
        else:
            return None

    def get_infocard(self):
        s = self.response.text
        p = r'<span class="infocard-lg-data text-muted">.*?</span>'
        m = re.search(p,s)
        if m:
            self.inforcard = m.group()
            return self.inforcard
        else:
            return None

    def get_small(self):
        s = self.inforcard
        # 所需資料在pokemon資料卡中故以資料卡(infocard)為範圍
        p = r'<small>.*?</small>'
        m = re.search(p,s)
        if m:
            self.small = m.group()
            return self.small
        else:
            return None

