import json

from flask import Flask, jsonify, request
from flask_cors import CORS

from FieldTemplateServer import FieldTemplate
from SqlAdapterServer import SqlAdapterServer

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示
CORS(app, resources=r'/*')

APPLICATION_JSON = "application/json;charset=UTF-8"
APPLICATION_TEXT = "application/txt"


@app.route("/api/field_template/selector", methods=["get"])
def fieldTemplateSelector():
    return app.response_class(response=json.dumps(FieldTemplate.apiSelector, ensure_ascii=False), status=200, mimetype=APPLICATION_JSON)


@app.route("/api/sql_adapter/selector", methods=["get"])
def sqlAdapterSelector():
    return app.response_class(response=json.dumps(SqlAdapterServer.apiSelector, ensure_ascii=False), status=200, mimetype=APPLICATION_JSON)


@app.route("/api/sql_adapter/execute", methods=["post"])
def sqlAdapterExecute():
    executor = SqlAdapterServer(request.args["type"], request.data.decode('utf-8'))
    return app.response_class(response=json.dumps(executor.execute(), ensure_ascii=False), status=200, mimetype=APPLICATION_TEXT)


@app.route("/api/field_template/execute", methods=["post"])
def fieldTemplateExecute():
    executor = FieldTemplate(content=request.data.decode('utf-8'), operator=request.args["type"])
    return app.response_class(response=executor.execute(), status=200, mimetype=APPLICATION_TEXT)


@app.route("/filed_template/test", methods=["get", "post"])
def field_template_test():
    field_template = FieldTemplate(content=request.data.decode('utf-8'))
    return field_template.field_template_test(url=request.args.get("url"), token=request.headers.get("Authorization"))


@app.route('/data', methods=['get', 'post'])
def get_data():
    # 获取URL中的参数，例：http://127.0.0.1:5000/data?page=1&limit=10，获取?后的数据
    print('URL中的参数：%s' % request.args)
    # 获取表单数据,即Content-Type为multipart/form-data的数据
    print('表单数据：%s' % request.form)
    # 获取Content-Type为application/json的数据
    print('application/json的数据：%s' % request.json)
    # 获取Content-Type为text/plain的数据
    print('text/plain的数据：%s' % request.data.decode('utf-8'))
    # 获取请求头
    print('请求头：%s' % request.headers)
    # 获取请求路径
    print('请求路径：%s' % request.path)
    # 获取user_agent
    print('user_agent：%s' % request.user_agent)
    # 获取请求地址
    print('请求地址：%s' % request.url)
    # 获取Cookies
    print('Cookies：%s' % request.cookies)
    # 获取认证数据
    print('认证数据：%s' % request.authorization)
    # 获取上传文件
    print('上传文件：%s' % request.files)
    # jsonify可返回list, dict等格式的数据
    return jsonify(request.json)
