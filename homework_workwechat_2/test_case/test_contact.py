import pytest
import yaml

from homework_workwechat_2.api.contact import Contact

userids = yaml.load(open("../file/userid.yaml", "r", encoding="utf-8"), Loader=yaml.BaseLoader)


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        user_data = self.contact.yaml_load("../file/user_data.yaml")
        self.userid = user_data.get("userid")
        self.name = user_data.get("name")
        self.mobile = user_data.get("mobile")
        self.department = user_data.get("department")
        self.alias = user_data.get("alias")
        self.mobile_update = user_data.get("mobile_update")

    @pytest.mark.parametrize("userid", userids)
    def test_get(self, userid):
        r = self.contact.get_member(userid)
        assert r.get("errcode") == 0

    def test_create(self):
        # 创建测试数据
        r = self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile,
                                       department=self.department,
                                       alias=self.alias)
        try:
            # 查找新建测试数据
            find_member = self.contact.get_member(self.userid)
        finally:
            # 删除测试数据
            self.contact.delete_member(self.userid)
        assert r.get("errcode") == 0 and find_member.get("errcode") == 0 and find_member.get("name", None) == self.name

    def test_update(self):
        # 创建测试数据
        self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile, department=self.department)
        # 更新测试数据
        r = self.contact.update_member(self.userid, mobile=self.mobile_update)
        try:
            # 查找测试数据
            find_member = self.contact.get_member(self.userid)
        finally:
            # 删除测试数据
            self.contact.delete_member(self.userid)
        assert r.get("errcode") == 0 and find_member.get("mobile") == self.mobile_update

    def test_delete(self):
        # 创建测试数据
        r = self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile,
                                       department=self.department)
        try:
            # 删除测试数据
            self.contact.delete_member(self.userid)
        finally:
            # 查询测试数据
            find_member = self.contact.get_member(self.userid)
        assert r.get("errcode") == 0 and find_member.get("errcode") == 60111
