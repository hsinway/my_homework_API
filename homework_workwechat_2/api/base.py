import requests
import yaml
from requests import Session


class Base:
    def __init__(self):
        token_data = self.yaml_load("../file/token.yaml")
        self.baseurl = "https://qyapi.weixin.qq.com/cgi-bin"
        self.cordid = token_data.get("cordid")
        self.corpsecrect = token_data.get("corpsecrect")
        self.s = Session()
        self.s.params["access_token"] = self.get_token().get("access_token", None)

    def get_token(self, corpid=None, corpsecrect=None):
        if corpid is None:
            corpid = self.cordid
        if corpsecrect is None:
            corpsecrect = self.corpsecrect
        params = {"corpid": corpid, "corpsecret": corpsecrect}
        r = requests.get(url=f'{self.baseurl}/gettoken', params=params)
        return r.json()

    def yaml_load(self, file_path):
        data = yaml.load(open(file_path, "r", encoding="utf-8"), Loader=yaml.BaseLoader) # BaseLoader 使纯数字变为字符串
        return data
