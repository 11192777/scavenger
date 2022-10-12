import json

from flask import Flask, jsonify, request

from FieldTemplateServer import FieldTemplate

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示


@app.route("/field_template/sql/mysql", methods=["get"])
def field_template_sql():
    field_template = FieldTemplate(content=request.data.decode('utf-8'), db_type="MYSQL")
    return field_template.get_sql()

@app.route("/field_template/sql/oracle", methods=["get"])
def field_template_sql():
    field_template = FieldTemplate(content=request.data.decode('utf-8'), db_type="ORACLE")
    return field_template.get_sql()


@app.route("/field_template/java", methods=["get"])
def field_template_java():
    field_template = FieldTemplate(content=request.data.decode('utf-8'))
    return field_template.get_java_enum()


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
