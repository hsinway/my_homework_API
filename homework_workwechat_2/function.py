import yaml
from faker import Faker


def fake_userids_create():
    userids = [Faker().bothify(text="?????##") for i in range(20)]
    yaml.dump(userids, open('./file/userid.yaml', 'w', encoding='UTF-8'))
