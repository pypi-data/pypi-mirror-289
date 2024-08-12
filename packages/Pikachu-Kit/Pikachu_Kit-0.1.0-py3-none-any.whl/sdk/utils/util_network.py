# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_network.py
@time: 2023/7/30 22:37
@desc:

"""
import requests
from .util_decorate import retry
from urllib3.exceptions import InsecureRequestWarning

# 禁用 InsecureRequestWarning 警告
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class NetWorkRequests(object):
    """
    NetWorkRequests
    """

    @retry(retry=3)
    def requests(self, url, headers=None, params=None, cookies=None, timeout=5,
                 data=None, json=None, method="POST", stream=False, proxies=None):
        """

        :param url:
        :param headers:
        :param params:
        :param cookies:
        :param timeout:
        :param data:
        :param json:
        :param method:
        :param stream:
        :param proxies:
        :return:
        """
        if method == "POST":
            response = requests.post(
                url=url,
                data=data,
                json=json,
                stream=stream,
                cookies=cookies,
                headers=headers,
                proxies=proxies,
                timeout=timeout,
                verify=False
            )
        elif method == "GET":
            response = requests.get(
                url=url,
                params=params,
                stream=stream,
                cookies=cookies,
                headers=headers,
                proxies=proxies,
                timeout=timeout,
                verify=False
            )
        else:
            raise ValueError("ERROR Methods {}".format(method))
        return response

    def download_videos(self, url, file, headers={}, proxies=None, max_size=1024 * 1024 * 5, method="GET"):
        """

        :param url:
        :param file:
        :param headers:
        :param max_size:
        :param method:
        :return:
        """
        res = {
            "status": -1,
            "url": url,
            "msg": "Failed",
            "result": []
        }
        status, response = self.requests(url, headers=headers, proxies=proxies,
                                         method=method)
        if not status:
            msg = "Failed"
        else:
            download_status_all = True
            content_len = int(response.headers["Content-Length"])
            nums = content_len // max_size if content_len % max_size == 0 else content_len // max_size + 1
            res["content_len"] = content_len
            res["split_nums"] = nums
            with open(file, "ab+") as fp:
                for i in range(nums):
                    start, end = i * max_size, (i + 1) * max_size
                    headers["Range"] = "bytes={}-{}".format(start, end)
                    chunk_status, response = self.requests(
                        url, headers=headers, proxies=proxies,
                        stream=True, method=method)
                    if not chunk_status:
                        download_status_all = False
                    else:
                        for chunk in response.iter_content(
                                chunk_size=max_size):
                            fp.seek(start)
                            fp.write(chunk)
                            fp.flush()
                    res["result"].append({
                        "status": chunk_status,
                        "during": [start, end],
                    })
            if download_status_all:
                msg = "Success"
                res["status"] = 0
            else:
                msg = "Failed"

        res["msg"] = msg

        return res
