import requests


# 获取企业微信通讯录token
def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwaad90cdf4a839085&corpsecret=4qvL5PohdlnCnQA3Sql7oyGxaK5UCBQLqoDRnTS-2fY')
    token = r.json()['access_token']
    return token


# 企业微信通讯录成员添加
def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "ceshi2"
        , "name": "测试第二号"
        , "mobile": "18723498370"
        , "department": [1, 2]
    }
    r = requests.post(url=create_member_url, json=data)
    print(r.json())
    assert 'created' == r.json()['errmsg']


# 企业微信通讯录成员删除
def test_delete_member():
    delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=ceshi2"
    r = requests.get(delete_member_url)
    print(r.json())
    assert 'deleted' == r.json()['errmsg']
