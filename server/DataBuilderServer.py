import datetime
import logging
import random
import threading
import uuid

import jsonpath

import RandomUtils
from DocumentServer import DocumentServer
from FormFieldServer import FormFieldServer
from FormServer import FormServer
from HermesServer import HermesServer


class DataBuilder(threading.Thread):
    def __init__(self, url, token, count):
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.count = count
        self.form_server = FormServer({"token": token, "archive_url": url})
        logging.info('===> Form server build successfully.')
        self.hermes_server = HermesServer({"token": token, "archive_url": url})
        logging.info('===> Hermes server build successfully.')
        self.form_field_server = FormFieldServer({"token": token, "archive_url": url})
        logging.info('===> Form field server build successfully.')
        self.document_server = DocumentServer({"token": token, "archive_url": url})
        logging.info('===> Document server build successfully.')
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.open_api_document_save()
        except Exception as e:
            logging.exception(e)

    def user_document_save(self):
        # 获取所有表单
        document_types = self.form_server.list_parents()
        logging.info('===> Successfully obtain document types. {}'.format(document_types))
        # 获取全部资料类型id
        all_document_type_ids = jsonpath.jsonpath(document_types, '$..documentTypeList..id')
        logging.info('===> All document type ids: {}'.format(all_document_type_ids))
        # 随机取 30 个资料类型id
        document_type_ids = RandomUtils.random_list(all_document_type_ids, 30)
        logging.info('===> Random document type ids:{}'.format(document_type_ids))
        # 获取所有公司
        company_list = self.hermes_server.list_companies()
        logging.info('===> Successfully obtain companies. {}'.format(company_list))
        # 获取前 10 个公司id
        company_ids = jsonpath.jsonpath(company_list, '$[:10].id')
        logging.info('===> Random companies company ids:{}'.format(company_ids))
        # 保密等级列表
        security_levels = ['CONFIDENTIAL', 'SECRET']
        cache_fields = {}
        for document_type_id in document_type_ids:
            cache_fields[document_type_id] = self.form_field_server.list_form_fields(document_type_id)

        for number in range(self.count):
            form_id = RandomUtils.random_one(document_type_ids)
            document = {'companyId': RandomUtils.random_one(company_ids),
                        'documentTypeId': form_id,
                        'attachmentList': [],
                        'securityLevelCode': RandomUtils.random_one(security_levels),
                        'documentFieldValueList': [],
                        'baseIsPaper': 'false'}
            for field in cache_fields[form_id]:
                widget_type = field['widgetType']
                widget_type_property = field['widgetTypeProperty']
                field_value = ''
                try:
                    if widget_type == 'TEXT_ARRAY':
                        field_value = '["{}"]'.format(field['code'])
                    elif widget_type == 'DATE':
                        data_format = field['widgetTypeProperty']['DATE_FORMAT']
                        if data_format == 'yyyy-MM-dd':
                            field_value = datetime.datetime.now().strftime('%Y-%m-%d')
                        elif data_format == 'yyyy-MM':
                            field_value = datetime.datetime.now().strftime('%Y-%m')
                        elif data_format == 'yyyy-MM-dd HH:mm:ss':
                            field_value = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    elif widget_type == 'BOOLEAN':
                        field_value = field['value']
                    elif widget_type == 'INTEGER':
                        field_value = '{}'.format(random.randint(int(widget_type_property['MIN_VALUE']), int(widget_type_property['MAX_VALUE'])))
                    elif widget_type == 'DOUBLE':
                        field_value = '{}'.format(random.uniform(float(widget_type_property['MIN_VALUE']), float(widget_type_property['MAX_VALUE'])))
                    else:
                        field_value = field['code']
                except RuntimeError:
                    field_value = ''
                document['documentFieldValueList'].append({'fieldId': field['id'], 'value': field_value})
            logging.info('===> The document is ready. {}'.format(document))
            self.document_server.save_document(document)
            logging.info('===> Document saved successfully.')

    def open_api_document_save(self):
        # 获取所有表单
        all_document_types = jsonpath.jsonpath(self.form_server.list_parents(), '$..documentTypeList.*')
        logging.info('===> Successfully obtain document types. {}'.format(all_document_types))
        # 随机取 30 个资料类型id
        document_types = RandomUtils.random_list(all_document_types, 30)
        logging.info('===> Random document types:{}'.format(document_types))
        # 获取所有公司
        company_list = self.hermes_server.list_companies()
        logging.info('===> Successfully obtain companies. {}'.format(company_list))
        # 获取前 10 个公司id
        company_codes = jsonpath.jsonpath(company_list, '$[:10].companyCode')
        logging.info('===> Random companies company codes:{}'.format(company_codes))
        # 保密等级列表
        security_levels = ['CONFIDENTIAL', 'SECRET']
        cache_fields = {}
        for document_type in document_types:
            cache_fields[document_type['code']] = self.form_field_server.list_form_fields(document_type['id'])

        for number in range(self.count):
            batch = []
            for batch_number in range(500):
                document_type_code = RandomUtils.random_one(document_types)['code']
                document = {'companyCode': RandomUtils.random_one(company_codes),
                            'documentTypeCode': document_type_code,
                            'originalNumber': document_type_code + '_' + str(datetime.datetime.now()),
                            'primaryField': str(uuid.uuid4()),
                            'securityLevelCode': RandomUtils.random_one(security_levels),
                            'fieldValueList': [],
                            'isPaper': 'false'}
                for field in cache_fields[document_type_code]:
                    widget_type = field['widgetType']
                    widget_type_property = field['widgetTypeProperty']
                    field_value = ''
                    try:
                        if widget_type == 'TEXT_ARRAY':
                            field_value = '["{}"]'.format(field['code'])
                        elif widget_type == 'DATE':
                            data_format = field['widgetTypeProperty']['DATE_FORMAT']
                            if data_format == 'yyyy-MM-dd':
                                field_value = datetime.datetime.now().strftime('%Y-%m-%d')
                            elif data_format == 'yyyy-MM':
                                field_value = datetime.datetime.now().strftime('%Y-%m')
                            elif data_format == 'yyyy-MM-dd HH:mm:ss':
                                field_value = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        elif widget_type == 'BOOLEAN':
                            field_value = field['value']
                        elif widget_type == 'INTEGER':
                            field_value = '{}'.format(
                                random.randint(int(widget_type_property['MIN_VALUE']), int(widget_type_property['MAX_VALUE'])))
                        elif widget_type == 'DOUBLE':
                            field_value = '{}'.format(
                                random.uniform(float(widget_type_property['MIN_VALUE']),
                                               float(widget_type_property['MAX_VALUE'])))
                        else:
                            field_value = field['code']
                    except RuntimeError:
                        field_value = ''
                    document['fieldValueList'].append({'fieldCode': field['code'], 'value': field_value})
                batch.append(document)
            logging.info('===> The document is ready. {}'.format(len(batch)))
            try:
                self.document_server.open_save_document(batch)
                logging.info('===> Document saved successfully.')
            except:
                logging.info('===> Failed but continue.')


if __name__ == '__main__':
    url = 'https://archive-stage.huilianyi.com'
    token = 'Bearer 4099ecd7-059b-4a53-b3e3-e7a983f4a386'
    # 并发数
    thread_num = 30
    # 一个线程推数批次，一批次500
    thread_generate_count = 2000000
    for i in range(thread_num):
        generate = DataBuilder(url, token, thread_generate_count)
        generate.start()
