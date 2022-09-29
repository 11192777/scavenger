import json
import logging
from itertools import groupby

import CommonUtils
from FormServer import FormServer


def get_business_type(business_type):
    if business_type == "会计档案":
        return "ACCOUNTANT"
    elif business_type == "人事档案":
        return "PERSONNEL"
    elif business_type == "综合档案":
        return "GENERAL"
    else:
        return None


def get_insert_form_sql(id, code, name, business_type):
    return "INSERT INTO ea_form (id, name, type, code, created_date, last_modified_date, tenant_id, created_by, last_modified_by, business_type) VALUES " \
           "('{}', '{}', 'DOCUMENT_TYPE_FIELD_TEMPLATE', '{}', NOW(), NOW(), '-1', '-1', '-1', '{}');\n".format(id, name, code, business_type)


def get_field_widget_type(widget_type):
    widget_type = widget_type.strip()
    if widget_type == "文本":
        return "TEXT"
    elif widget_type == "文本数组":
        return "TEXT_ARRAY"
    elif widget_type == "整数":
        return "INTEGER"
    elif widget_type == "布尔":
        return "BOOLEAN"
    elif widget_type == "浮点数":
        return "DOUBLE"
    elif widget_type == "日期":
        return "DATE"
    elif widget_type == "超链接":
        return "HYPERLINK"
    elif widget_type == "长文本":
        return "LONG_TEXT"
    else:
        return None


def get_boolean(value):
    if value == "是":
        return "TRUE"
    else:
        return "FALSE"


def get_field_widget_type_property(field):
    widget_type = get_field_widget_type(field["类型*"])
    widget_type_property = {}
    if widget_type == "TEXT" or widget_type == "HYPERLINK" or widget_type == "LONG_TEXT":
        widget_type_property = {"WORDS_LIMIT": field["格式范围"]}
    elif widget_type == "INTEGER" or widget_type == "DOUBLE":
        widget_type_property = {"MIN_VALUE": str(field["格式范围"]).split("_")[0], "MAX_VALUE": str(field["格式范围"]).split("_")[1]}
    elif widget_type == "DATE":
        widget_type_property = {"DATE_FORMAT": "yyyy-MM-dd", "DATE_FORMAT_WEB": "YYYY-MM-DD"}
    elif widget_type == "TEXT_ARRAY":
        widget_type_property = {"ITEM_WORDS_LIMIT": str(field["格式范围"]).split("/")[1], "ITEMS_LIMIT": str(field["格式范围"]).split("/")[0]}
    else:
        return None
    return json.dumps(widget_type_property)


def get_form_sql(form_id):
    return '''DELETE eff.* FROM ea_form ef JOIN ea_form_field eff ON ef.id = eff.form_id
WHERE ef.id = '{}';  #删除配置字段
DELETE ef.*  FROM ea_form ef
WHERE ef.id = '{}';  #删除模板\n'''.format(form_id, form_id, form_id)


def get_insert_field_sql(field, form_id, field_sort_number):
    return "INSERT INTO ea_form_field (name, code, form_id, widget_type, sort_number, required, volume_primary_key, input_manually, tenant_id, created_date, last_modified_date, created_by, last_modified_by, widget_type_property) " \
           "VALUES ('{}', '{}', '{}', '{}', {}, {}, {}, {}, '-1', NOW(), NOW(),  '-1', '-1', '{}');\n" \
        .format(field["字段名称*"], field["字段编码*"], form_id, get_field_widget_type(field["类型*"]), field_sort_number, get_boolean(field["是否必填*"]), get_boolean(field["是否成册主键"]), get_boolean(field["是否支持编辑*"]), str(get_field_widget_type_property(field)).replace(" ", ""))


class FieldTemplate:

    def __init__(self, content: str):
        self.fields_by_form = None
        self.content_csv = None
        self.title_csv = None
        self.content = content

    def format_title_csv(self):
        titles = self.content.split('\n')[0]
        logging.info("===> Field template title:{}".format(titles))
        title_csv = []
        for title in titles.split('\t'):
            if title == '':
                continue
            else:
                title_csv.append(title)
        logging.info("===> Success obtain title csv:{}".format(title_csv))
        self.title_csv = title_csv

    def format_content_csv(self):
        content_csv = []
        rows = self.content.split('\n')
        rows = [row for row in rows if row.strip()]
        for row_num in range(1, len(rows)):
            items = rows[row_num].split('\t')
            logging.info("===> Row:{} items:{}".format(row_num, items))
            content = {}
            for index in range(min(len(items), len(self.title_csv))):
                content[self.title_csv[index]] = items[index]
            logging.info("===> CSV obtain successfully:{}".format(content))
            content_csv.append(content)
        self.content_csv = content_csv

    def get_sql(self):
        sql = ''
        form_id = 10

        for form, fields in self.format_content():
            sql = sql + "# {}字段模板\n".format(form[1])
            sql = sql + get_form_sql(form_id)
            sql = sql + get_insert_form_sql(form_id, form[0], form[1], get_business_type(form[2]))
            field_sort_number = 0
            for field in list(fields):
                sql = sql + get_insert_field_sql(field, form_id, field_sort_number)
                field_sort_number = field_sort_number + 1
            form_id = form_id + 1
            sql = sql + "\n\n"
        return sql

    def get_java_enum(self):
        line = '''\n
    /**
     * {}
     */
    {}("{}", "{}", BusinessEnvironmentEnum.{})'''
        lines = []
        for form, fields in self.format_content():
            lines.append(line.format(form[1], form[0], form[0], form[1], get_business_type(form[2])))
        java = '''package com.huilianyi.earchives.business.enumeration;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NonNull;
import org.apache.commons.lang3.StringUtils;

import javax.annotation.Nullable;
import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * <p>
 * 字段模板枚举
 * </P>
 *
 * @Author Qingyu.Meng
 * @Date 2021/7/9 14:00
 * @Version 1.0
 */
@Getter
@AllArgsConstructor
public enum FieldTemplateEnum {{{};


    private final String code;
    private final String name;
    private final BusinessEnvironmentEnum businessEnvironment;

    /**
     * 根据key获取字段模板枚举
     *
     * @param code this.code
     * @return FieldTemplateEnum
     */
    @Nullable
    public static FieldTemplateEnum parseCode(String code) {{
        if (StringUtils.isBlank(code)) {{
            return null;
        }}

        for (FieldTemplateEnum fieldTemplateEnum : FieldTemplateEnum.values()) {{
            if (fieldTemplateEnum.code.equals(code)) {{
                return fieldTemplateEnum;
            }}
        }}

        return null;
    }}

    /**
     * 根据key获取字段模板枚举
     *
     * @param name this.key
     * @return FieldTemplateEnum
     */
    @Nullable
    public static FieldTemplateEnum parseName(String name) {{
        if (StringUtils.isBlank(name)) {{
            return null;
        }}

        for (FieldTemplateEnum fieldTemplateEnum : FieldTemplateEnum.values()) {{
            if (fieldTemplateEnum.name.equals(name)) {{
                return fieldTemplateEnum;
            }}
        }}

        return null;
    }}

    /**
     * 根据code获取name
     *
     * @param code this.code
     * @return FieldTemplateEnum
     */
    @Nullable
    public static String getNameByCode(String code) {{
        FieldTemplateEnum fieldTemplateEnum = parseCode(code);
        return fieldTemplateEnum == null ? null : fieldTemplateEnum.getName();
    }}

    /**
     * 根据name获取code
     *
     * @param name this.name
     * @return FieldTemplateEnum
     */
    @Nullable
    public static String getCodeByName(String name) {{
        FieldTemplateEnum fieldTemplateEnum = parseName(name);
        return fieldTemplateEnum == null ? null : fieldTemplateEnum.getCode();
    }}

    /**
     * <H2>获取业务环境下的模板</H2>
     *
     * @param businessEnv 业务环境
     * @return {{@link java.util.Set<com.huilianyi.earchives.business.enumeration.FieldTemplateEnum>}}
     * @author Qingyu.Meng
     * @since 2022/8/31
     */
    public static Set<FieldTemplateEnum> getFieldTemplates(@NonNull BusinessEnvironmentEnum businessEnv) {{
        return Arrays.stream(FieldTemplateEnum.values()).filter(template -> template.getBusinessEnvironment().equals(businessEnv)).collect(Collectors.toSet());
    }}

}}
'''.format(",".join(lines))
        return java

    def format_content(self):
        self.format_title_csv()
        self.format_content_csv()
        sorted(self.content_csv, key=lambda line: (line["资料类型编码*"], line["资料名称*"], line["模板类型"]))
        return groupby(self.content_csv, key=lambda line: (line["资料类型编码*"], line["资料名称*"], line["模板类型"]))

    def field_template_test(self, url, token):
        form_server = FormServer(env_url=url, token=token)
        business_envs = ['ACCOUNTANT', 'PERSONNEL', 'GENERAL']
        for business_env in business_envs:
            logging.info('===> Create archive type. Business env:{}'.format(business_env))
            archive_data = {
                "code": CommonUtils.print_now_time(),
                "name": CommonUtils.print_now_time(),
                "retentionPeriod": "30",
                "businessType": business_env,
                "isEnabled": "true",
                "sortNumber": 99999999
            }
            archive_type = form_server.save_form(archive_data)
            archive_type_id = archive_type['id']
            logging.info('===> The archive type was created successfully.')
            logging.info('===> Gets the field template under the business dev：{}'.format(business_env))
            field_templates = form_server.get_field_templates(business_env)
            field_template_codes = [item.data('code') for item in field_templates]
            logging.info('===> Field template obtained successfully. {}'.format(field_template_codes))
            for field_template_code in field_template_codes:
                document_date = {
                    "code": CommonUtils.print_now_time(),
                    "name": CommonUtils.print_now_time(),
                    "isEnabled": "true",
                    "securityLevelCode": "TOP_SECRET",
                    "parentId": archive_type_id,
                    "businessType": field_template_code,
                    "sortNumber": 9999999
                }
                logging.info('===> Start creating document types. Field template is :{}'.format(field_template_code))
                document_type = form_server.save_form(document_date)
                if document_type is not None:
                    logging.info('===> The archive type was created successfully.')
            logging.info('===> Delete the {} archive type.'.format(business_env))
            form_server.delete_form(archive_type_id)
            logging.info('===> Delete the {} archive type successfully.'.format(business_env))
        return "SUCCESS"
