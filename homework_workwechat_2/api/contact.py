from typing import List

from homework_workwechat_2.api.base import Base


class Contact(Base):
    def get_member(self, userid):
        params = {"userid": userid}
        r = self.s.get(url=f'{self.baseurl}/user/get', params=params)
        return r.json()

    def update_member(self, userid: str, mobile: str, **kwargs):
        data = {
            "userid": userid
            , "mobile": mobile
        }
        data.update(kwargs)
        r = self.s.post(url=f'{self.baseurl}/user/update', json=data, headers='')
        return r.json()

    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        data = {
            "userid": userid
            , "name": name
            , "mobile": mobile
            , "department": department
        }
        data.update(kwargs)
        r = self.s.post(url=f'{self.baseurl}/user/create', json=data)
        return r.json()

    def delete_member(self, userid):
        params = {"userid": userid}
        r = self.s.get(url=f'{self.baseurl}/user/delete', params=params)
        return r.json()
