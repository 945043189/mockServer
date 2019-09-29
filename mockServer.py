# /usr/bin/env python
# -*- coding:utf-8 -*-

# 1分钟搭建极简mock server，参考：https://www.cnblogs.com/mikasama/p/9838480.html

# 打包exe可执行文件：https://jingyan.baidu.com/article/6b97984df6f4501ca2b0bf29.html

from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

tasks = {
    "code": 0,
    "msg": "OK",
    "data": {
        "waybillNumber": "1526351",
        "serviceMode": "10",
        "waybillStatus": "10",
        "deliveryAbbreviationAddress": "深圳",
        "pickupAbbreviationAddress": "深圳"
    },
    "traceId": "dp1r"
}

helloWorld = {
    "code": 0,
    "msg": "OK",
    "data": {
        "name": "zaj",
        "company": "steelgt",
        "waybillStatus": "10",
        "deliveryAbbreviationAddress": "深圳",
        "pickupAbbreviationAddress": "深圳"
    },
    "traceId": "dp1r"
}


@app.route('/helloWorld', methods=['GET', 'POST'])
def get_helloWorld():
    return jsonify(helloWorld)


@app.route('/tasks', methods=['GET', 'POST'])
def get_task():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=6868,
        debug=True
    )
