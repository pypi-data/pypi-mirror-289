#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tools.py
@Time    :   2024/01/08 16:08:00
@Author  :   qingfeng7
@Version :   1.0
@Contact :   qingfeng7@staff.sina.com.cn
@Desc    :   一些常用的工具文件方法
'''

# here put the import lib
import logging.handlers
import logging
import requests
import os
import json
import glob
import traceback
from datetime import datetime
import sys


base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class sinaTools():
    VERSION=1.0

    def __init__(self, log=None):
        if log:
            self.log = log
        
            
    def send_alarm(self, users, group=None, title=None, content=None):
        '''发送报警信息'''
        if not isinstance(users, list):
            users = [users]
        params = {
            'title': title,
            'content': content,
            'sendto': ','.join(users),
            'group': group,
        }
        url = 'http://falcon.search.weibo.com/falcon/intfs/Alarm/sendAlarm'
        res = requests.post(url, params=params)
        return res.text


    def get_hot_query(self, nums=50, day=None):
        """
        获取某天的热搜词汇
        nums: 获取的数量
        day: 默认为None, 可以输入日期查找, 目前只能是当天的
        """
        if not os.path.exists('./datas'):
            os.mkdir('./datas')
        os.system(
            'rsync 10.185.30.215::MINI_SEARCH/IntentionFinder/data/query_intention/hotsearch_words.txt ./datas/')
        with open('./datas/hotsearch_words.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()  

        return [i.strip() for i in lines[:nums]]

    def get_query(self, nums=50, day=None):
        """
        获取某天的普搜词汇
        nums: 获取的数量
        day: 默认为None, 可以输入日期查找
        """
        if not os.path.exists('./datas/rand_query'):
            os.mkdir('./datas/rand_query')
        os.system('rsync 10.2.22.72::MINI_SEARCH/zhigang11/rand_query/* ./datas/rand_query/')

        # 查找./datas/rand_query/路径下所有以txt结尾的文件并读取
        files = glob.glob('./datas/rand_query/*.txt')
        lines = []
        for f in files:
            with open(f, 'r', encoding='utf-8') as f:
                try:
                    raw_lines = f.readlines()
                    line = [i.strip().split('\t')[0] for i in raw_lines
                            if i.strip().split('\t')[2]!=2]
                    lines.extend(line)
                    break
                except Exception as e:
                    traceback.print_exc()
                    self.log.error(e)
        return lines[:nums]


    def get_mid_by_query(self, query, pages=3):
        """
        通过query获取mid, 这个是ac的接口
        query 查询的关键词
        """
        mid_list = []
        if isinstance(query, str):
            query = [query]
        for ele in query:
            for page in range(pages):
                try:
                    line = ele.strip()
                    url = "http://i.search.weibo.com/search/intra.php?sid=t_wap_ios&cuid=123456789&us=1&page={}&count=10&istag=2&key={}&simplify=1&xsort=social&z=all&cluster_repost=0&socialtime=1&no_continuous=1".format(
                        page+1, line)
                    req = requests.get(url)
                    res = req.text
                    res = json.loads(res)
                    if not isinstance(res, dict):
                        continue
                    for item in res['us']:
                        if item.get('category', 0) == 26 or item.get('category', 0) == 28:
                            mid_list += [middoc.get('ID') for middoc in item.get('subposdata', [])]
                except Exception as e:
                    traceback.print_exc()
                    self.log.error(e)
        return mid_list


    def get_weibo_from_hbase(self, mid):
        """从hbase中读取到内容"""
        try:
            _url = "http://getdata.search.weibo.com/getdata/querydata.php?condition=%s&mode=weibo&format=json&hbase=1" % mid
            r = requests.get(_url)
            ret = r.json()
            return ret
        except:
            return {}


    def get_weibo_from_bs(self, mid, ip_list, port, base_url=None, print_url=False, all_url=False):
        """
        从bs中读取博文相关内容
        mid 要读取的博文的mid
        ip_list bs 数据库的IP地址
        port bs 数据库的端口号
        """
        base_url = 'http://i.search.weibo.com/search/libac.php?query=x_nocsort:1 x_dup:1 id:{},&ip={}&port={}'
        info = {}
        for ip in ip_list:
            url = base_url.format(mid, ip, port)
            try:
                res = requests.get(url)
                r = res.json()
            except:
                traceback.print_exc()
                self.log.info('{} url ERROR: mid: {}, url: {}, error_msg: {}'.format(
                    datetime.now(), mid, url, res.text))
                r = {}
            if 'sp' not in r:
                continue
            r = r['sp']
            if 'result' in r and r['result']:
                info = r['result'][0]
                if print_url:
                    print(f'{ip}\t{url}')
                if not all_url:
                    return info
        return info

    def get_ip_list(self, tree_id):
        """
        获取服务相关的IP地址 
        tree_id 表示的 http://falcon.search.weibo.com/ops/cmdb?tree_id=3700
        return 返回该节点配置的所有的ip地址
        """
        url = 'http://falcon.search.weibo.com/falcons/intfs/Node/getServers?tree_id={}'.format(
            tree_id)
        res = requests.get(url)
        r = json.loads(res.text)
        if 'data' in r:
            return r['data']
        else:
            return []


    def get_weibo_from_summary(self, mid, ip_list, ports, base_url=None):
        """
        从摘要库中中获取微博内容
        ips = ["10.85.39.194", "10.85.39.193", "10.85.39.191"]
        """
        if not base_url:
            base_url = "http://i.search.weibo.com/search/libac.php?query=x_nocsort:1%20x_dup:1%20id:{}&ip={}&port={}"
    
        info = {}
        for ip, p in zip(ip_list, ports):
            url = base_url.format(
                mid, ip, p)
            res = requests.get(url)
            res = res.json()
            if 'sp' not in res:
                continue
            res = res['sp']
            if 'result' in res and res['result']:
                info = res['result'][0]
        return info
    

    def get_attribute_from_bowen(self, bowen, attribute):
        """
            解析博文，从博文中获取字典中的值
            bowen json 
            attribute list  
        """
        if not isinstance(attribute, list):
            attribute = [attribute]
        for att in attribute:
            if att in bowen:
                bowen = bowen.get(att)
            else:
                return None
        return bowen
    
    
    def get_attr_by_mid(self, mid, keys:list) -> list:
        """
        获取微博中的字段通过mid
        mid 微博的mid
        attribute list, 如果要获取的值是多重嵌套
            在 keys 里面可以添加[url, [all_tag_new, m1]] 这种获得url和r3
        """
        dic = self.get_weibo_from_hbase(mid)
        if not dic:
            return []
        if not keys:
            return []
        res = []
        for att in keys:
            if isinstance(att, list):
                temp_dic = dic
                for li in att:
                    if not isinstance(temp_dic, dict):
                        temp_dic = json.loads(temp_dic)
                        
                    temp_dic = temp_dic.get(li)
                res.append(temp_dic)
            else:
                res.append(self.get_attribute_from_bowen(dic, att))
        return res


class wenxinTool():
    def __init__(self, api_key, secret_key) -> None:
        self.api_key = api_key
        self.secret_key = secret_key

    def __get_wenxing_access_token(self, api_key, secret_key):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """

        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    def cat_wenxing(self, question):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + \
            self.__get_wenxing_access_token(self.api_key, self.secret_key)

        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "stream": True
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, stream=True)
        res = []
        for line in response.iter_lines():
            res.append(line)
        return res
    


class logger:
    def __init__(self, log_dir='./logs', log_name='app.log', max_size=1024*1024*10, backup_count=5):
        """
        :param log_dir: 日志文件存储目录
        :param log_name: 日志文件名
        :param max_size: 单个日志文件最大大小，单位字节，默认10MB
        :param backup_count: 保留的旧日志文件数量，默认5个
        """
        self.log_dir = log_dir
        self.log_path = os.path.join(self.log_dir, log_name)
        self.max_size = max_size
        self.backup_count = backup_count

        # 创建日志文件夹
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # 创建logger
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            # 文件控制器
            file_handler = logging.handlers.RotatingFileHandler(
                self.log_path, maxBytes=self.max_size, backupCount=self.backup_count)
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            # 控制台输出
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)  # 控制台输出仅为INFO级别
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def info(self, message):
        """记录INFO级别日志"""
        self.logger.info(message)

    def debug(self, message):
        """记录DEBUG级别日志"""
        self.logger.debug(message)

    def warning(self, message):
        """记录WARNING级别日志"""
        self.logger.warning(message)

    def error(self, message):
        """记录ERROR级别日志"""
        self.logger.error(message)

    def delete_old_logs(self):
        """
        删除旧的日志文件，只保留backup_count指定的数量的日志文件
        """
        log_files = glob.glob(os.path.join(self.log_dir, '*.log'))
        log_files.sort(key=os.path.getmtime, reverse=True)

        for log_file in log_files[self.backup_count:]:
            os.remove(log_file)

