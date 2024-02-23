def getDateDim(var):
    if var == '日':
        return 1
    elif var == '月':
        return 3
    elif var == '周':
        return 2
    else:
        raise ValueError('参数错误')


def getAreaDim(var):
    if var == '全国':
        return 5
    elif var == '仓库':
        return 2
    elif var == '门店':
        return 1
    else:
        raise ValueError('参数错误')
    
    
def getConfig():
    json = '''{{
    "|skg^0^BizDailyCollaboratingComponent|":{{
        "filters":[
            {{
                "name":"filter",
                "type":"TableMultiFilter"
            }}
        ],
        "toolbar":[
            {{
                "children":[
                    {}
                ],
                "type":"download"
            }},
            {{
                "children":[
                   {}
                ],
                "type":"upload"
            }}
        ],
        "formArea":[
            {{
                "key":"scItemName",
                "name":"scItemName",
                "title":"货品名称",
                "type":"string"
            }},
            {{
                "key":"pageSize",
                "name":"pageSize",
                "title":"Page Size",
                "value":"1",
                "type":"string"
            }},
            {{
                "key":"scItemIdList",
                "name":"scItemIdList",
                "title":"69码",
                "type":"string",
                "x-component":"BatchInput",
                "x-props":{{
                    "maxLength":200,
                    "max":200,
                    "openChineseInput":true
                }}
            }},
            {{
                "key":"brands",
                "name":"brands",
                "title":"品牌",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/brand/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"firstCategoryCodeList",
                "name":"firstCategoryCodeList",
                "title":"供应链大类",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/category/sc_category_list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"selfCategoryPathList",
                "name":"selfCategoryPathList",
                "title":"自建类目",
                "type":"string",
                "x-component":"LazySelect",
                "x-props":{{
                    "lazyLoad":false,
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":true,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/category/list?dataStructure=tree",
                    "hasClear":true
                }}
            }},
            {{
                "key":"itemLevelList",
                "name":"itemLevelList",
                "title":"供应商品分层",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/level/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"lifeCycleList",
                "name":"lifeCycleList",
                "title":"供应采购状态",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/lifeCycle/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"etyParam1List",
                "name":"etyParam1List",
                "title":"69码",
                "type":"string",
                "x-component":"BatchInput",
                "x-props":{{
                    "maxLength":200,
                    "max":200,
                    "openChineseInput":true,
                    "isArrayValue":true
                }}
            }},
            {{
                "key":"etyParam10List",
                "name":"etyParam10List",
                "title":"商品类型",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/setLevel/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"attrRelParam1List",
                "name":"attrRelParam1List",
                "title":"负责人",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/reportChannel/manager_list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"attrRelCode1List",
                "name":"attrRelCode1List",
                "title":"渠道货主",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/channel/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"attrRelParam3List",
                "name":"attrRelParam3List",
                "title":"仓库",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/warehouse/list",
                    "hasClear":true
                }}
            }},
            {{
                "enum":[
                    {{
                        "label":"主品",
                        "value":"0"
                    }},
                    {{
                        "label":"赠品",
                        "value":"1"
                    }}
                ],
                "name":"attrRelParam4List",
                "key":"attrRelParam4List",
                "title":"主赠品",
                "x-component":"RequestSelect",
                "x-props":{{
                    "hasClear":true
                }}
            }},
            {{
                "key":"channelCodeList",
                "name":"channelCodeList",
                "title":"提报单位",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"planbasic://api/plan/reportChannel/list",
                    "hasClear":true
                }}
            }},
            {{
                "key":"shop",
                "name":"shop",
                "title":"渠道店铺",
                "type":"RequestSelect",
                "x-props":{{
                    "autoSelectAfterLoad":false,
                    "filterLocal":true,
                    "maxTagCount":8,
                    "showPath":false,
                    "showSearch":true,
                    "mode":"multiple",
                    "placeholder":"",
                    "url":"",
                    "hasClear":true
                }}
            }},
            {{
                "enum":[
                    {{
                        "label":"预测波动性大",
                        "value":"3"
                    }}
                ],
                "name":"alertType",
                "key":"alertType",
                "title":"指标筛选",
                "x-component":"RequestSelect",
                "x-props":{{
                    "hasClear":true
                }}
            }},
            {{
                "default":"1",
                "x-component":"RequestSelect",
                "name":"dateDimType",
                "sort":8,
                "title":"时间范围",
                "key":"dateDimType",
                "x-props":{{
                    "hasClear":false,
                    "url":"salesplan-business://webapi/salesplan/common/option/datedim/getList"
                }}
            }},
            {{
                "x-component":"dateRange",
                "x-mega-props":{{
                    "span":2
                }},
                "name":"[startDate,endDate]",
                "sort":8,
                "title":"具体日期",
                "key":"startEnd"
            }}
        ],
        "headerOperation":{{
            "config":{{
                "timeDimType":2,
                "viewDimType":"9"
            }},
            "dataSource":[
                {{
                    "name":"salesPredictTime",
                    "style":{{
                        "color":"#999999",
                        "font-size":"12px"
                    }},
                    "title":"预测时间 ",
                    "site":"right",
                    "type":"String"
                }},
                {{
                    "site":"right",
                    "key":"viewDimType",
                    "name":"viewDimType",
                    "title":"视角",
                    "type":"Select",
                    "dataSource":[
                        {{
                            "label":"品",
                            "areaDimType":5,
                            "channelDimType":2,
                            "value":"9"
                        }},
                        {{
                            "label":"品+提报单位",
                            "areaDimType":5,
                            "channelDimType":3,
                            "value":"7"
                        }},
                        {{
                            "label":"品+仓",
                            "areaDimType":2,
                            "channelDimType":2,
                            "value":"5"
                        }},
                        {{
                            "label":"品+渠道货主",
                            "areaDimType":5,
                            "channelDimType":1,
                            "value":"3"
                        }},
                        {{
                            "label":"品+提报单位+仓",
                            "areaDimType":2,
                            "channelDimType":3,
                            "value":"10"
                        }}
                    ]
                }},
                {{
                    "name":"timeDimType",
                    "key":"timeDimType",
                    "title":"",
                    "site":"right",
                    "type":"ButtonGroup",
                    "value":[
                        {{
                            "checked":false,
                            "label":"月",
                            "value":3
                        }},
                        {{
                            "checked":true,
                            "label":"周",
                            "value":2
                        }},
                        {{
                            "checked":false,
                            "label":"日",
                            "value":1
                        }}
                    ]
                }}
            ]
        }},
        "listQuery":{{
            "method":"post",
            "url":"salesplan-business://webapi/salesplan/daily/collaborating/scitem/doGetMainPage4Collaborate"
        }},
        "pageSize":10,
        "pageSizeList":[
            10,
            20,
            50
        ]
    }}
}}'''


if __name__ == '__main__':

    url = '''http://planbiz.lydaas.com/ascp-tools-gei/gei/import/template/salesPlan_business_country_channel_week_saas_import?query={{"iframeContainerFrom":"plan-dchain","__IFRAME_CONTAINER_IFRAME_ID__":"3","dateDimType":{{}},"timeDimType":{{}},"viewDimType":"9","channelDimType":2,"code":"{{}}","componentCode":"BizDailyCollaboratingComponent","entityType":"{{}}","entityTypes":[{{}}],"tenantCode":"vinda","bizMode":99,"areaDimType":{{}},"tabCode":"scItem"}}''';

    print(url.format(getDateDim("日"), getDateDim("日"), "salesPlanDetail_scItem_country_day_import", 24, 24,
                     getAreaDim("全国")))
    print(url.format(getDateDim("周"), getDateDim("周"), "salesPlanDetail_scItem_country_week_import", 24, 24,
                     getAreaDim("全国")))
    print(url.format(getDateDim("月"), getDateDim("月"), "salesPlanDetail_scItem_country_month_import", 24, 24,
                     getAreaDim("全国")))
    print(url.format(getDateDim("日"), getDateDim("日"), "salesPlanDetail_scItem_warehouse_day_import", 24, 24,
                     getAreaDim("仓库")))
    print(url.format(getDateDim("周"), getDateDim("周"), "salesPlanDetail_scItem_warehouse_week_import", 24, 24,
                     getAreaDim("仓库")))
    print(url.format(getDateDim("月"), getDateDim("月"), "salesPlanDetail_scItem_warehouse_month_import", 24, 24,
                     getAreaDim("仓库")))

    print()

    print(url.format(getDateDim("日"), getDateDim("日"), "salesPlanDetail_scItem_country_day_import", 25, 25,
                     getAreaDim("全国")))
    print(url.format(getDateDim("周"), getDateDim("周"), "salesPlanDetail_scItem_country_week_import", 25, 25,
                     getAreaDim("全国")))
    print(url.format(getDateDim("月"), getDateDim("月"), "salesPlanDetail_scItem_country_month_import", 25, 25,
                     getAreaDim("全国")))
    print(url.format(getDateDim("日"), getDateDim("日"), "salesPlanDetail_scItem_warehouse_day_import", 25, 25,
                     getAreaDim("仓库")))
    print(url.format(getDateDim("周"), getDateDim("周"), "salesPlanDetail_scItem_warehouse_week_import", 25, 25,
                     getAreaDim("仓库")))
    print(url.format(getDateDim("月"), getDateDim("月"), "salesPlanDetail_scItem_warehouse_month_import", 25, 25,
                     getAreaDim("仓库")))