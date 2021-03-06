# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_getVideoLabelAndTopic(unittest.TestCase):
    """查看视频详情,获取该视频的标签和话题"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1OTg3NjksImV4cCI6MTU3MTE5MDc2OSwiYmFja191c2VyX2lkIjo2NjYsImlzcyI6InFpYW9rdV9iYWNrIn0.30i2L4PyCQ6kyF_aZ-8Ba2_4NxJAqmh7SL8p_1eiXPY"
    def test(self):
        pass

    def tearDown(self):
        # pass
        # 修改后台上传的视频
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """查看视频详情,获取该视频的标签和话题"""
        data = {
            "videoId":"627169188108042240",
        }
        backHttp.getVideoLabelAndTopic(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "videoId":"627169188108042240",
        }
        backHttp.getVideoLabelAndTopic(data)


if __name__ == '__main__':
    unittest.main()

