import json
import time
import requests
from requests.cookies import RequestsCookieJar
from utils import RandomUtils


class Login:
    def __init__(self, envTag="f2c74ef4"):
        self.headers = {"Content-Type": "application/json", "linked_env_tag": envTag}
        self.cookies = RequestsCookieJar()

    def doLogin(self, account, password, envTag):
        url = "https://sit-auth.zacz.cn/api/doLogin"
        data = {
            "loginType": 0,
            "password": password,
            "account": account,
            "product": "QuickStock",
            "goods": "erp_quickstock",
            "channel": None,
            "redirect_uri": ""
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(data), cookies=self.cookies)
        self.cookies.update(response.cookies)
        self.cookies.set("bizphin_auth_token", self.cookies.get("bizphin_auth_center_token"))
        if envTag:
            self.cookies.set("linked_env_tag", envTag)
        print("===> login result:{}".format(response.json()))

        refresh = self.refresh()
        if refresh.json()["errorMessage"]:
            self.headers["x-xsrf-token"] = refresh.cookies.get("XSRF-TOKEN")
            self.cookies.update(refresh.cookies)

    def refresh(self):
        url = "https://omssaas-sit.zacz.cn/api/erp_order/create_order_api"
        return requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps({}))


class Order:

    def __init__(self, account, password, envTag=None):
        login = Login()
        login.doLogin(account, password, envTag)
        self.headers = login.headers
        self.cookies = login.cookies

    def create(self, qty=1):
        url = "https://omssaas-sit.zacz.cn/api/erp_order/create_order_api"
        data = {
            "receiver": {
                "deliveryType": {
                    "label": "快递配送",
                    "value": 1
                },
                "name": "Mrna-me",
                "contactNumber": "13777777777",
                "harvestAddress": [
                    {
                        "childElements": [
                            {
                                "childElements": [
                                    {
                                        "code": "310107",
                                        "name": "普陀区"
                                    }
                                ],
                                "code": "310100",
                                "name": "上海市",
                                "next": {
                                    "code": "310107",
                                    "name": "普陀区"
                                }
                            }
                        ],
                        "code": "310000",
                        "name": "上海",
                        "next": {
                            "childElements": [
                                {
                                    "code": "310107",
                                    "name": "普陀区"
                                }
                            ],
                            "code": "310100",
                            "name": "上海市",
                            "next": {
                                "code": "310107",
                                "name": "普陀区"
                            }
                        }
                    }
                ],
                "detailAddress": "长风新村街道金沙江路1000号",
                "deliveryTypeId": 1,
                "deliveryTypeName": "快递配送",
                "provinceCode": "310000",
                "province": "上海",
                "cityCode": "310100",
                "city": "上海市",
                "districtCode": "310107",
                "district": "普陀区"
            },
            "organizationInfo": {},
            "invoice": {
                "open": False
            },
            "salesBusiness": "retail",
            "orderType": "normal",
            "orderFrom": "manualCreate",
            "extCreateTime": RandomUtils.random_time("%Y-%m-%d %H:%M:%S"),
            "postFee": 0,
            "totalDiscountFee": 0,
            "actualTotalPrice": 6,
            "shouldPayFee": 6,
            "salesBusinessText": "零售业务",
            "storeId": "1000000004022925",
            "warehouse": {
                "deep": 0,
                "value": "1000100393",
                "label": "yubaby(yubaby)",
                "code": "yubaby",
                "type": 3,
                "features": {
                    "enableNegative": "0"
                },
                "model": 1,
                "id": "1000100393",
                "wmsType": "0",
                "name": "yubaby",
                "status": 1
            },
            "addressTool": "长风新村街道金沙江路1000号，13777777777，Mrna me",
            "orderLines": [
                {
                    "inputVText": "coke",
                    "salesPrice": "3.00",
                    "skuTypeList": [
                        0
                    ],
                    "type": 0,
                    "baseUnit": {
                        "unitName": "瓶",
                        "scItemId": "581594449823932681",
                        "label": "瓶",
                        "unitId": "576153968434971902",
                        "relationNum": 1,
                        "value": "576153968434971902"
                    },
                    "itemName": "肥肠自动化可乐勿动",
                    "virtualStr": "否",
                    "merchantId": "3592",
                    "price": "3.00",
                    "id": "581594449823932681",
                    "brandName": "测测测",
                    "unitName": "瓶",
                    "scItemId": "581594449823932681",
                    "tags": [],
                    "taxRate": "4",
                    "itemId": "581594449823932681",
                    "brandId": "579424657875751047",
                    "skuCode": "coke",
                    "status": 1,
                    "basicUnitId": "576153968434971902",
                    "virtual": 0,
                    "scItemSpecList": [
                        {
                            "unitName": "瓶",
                            "scItemId": "581594449823932681",
                            "label": "瓶",
                            "unitId": "576153968434971902",
                            "relationNum": 1,
                            "value": "576153968434971902"
                        }
                    ],
                    "code": "coke",
                    "itemProperty": "coke",
                    "title": "肥肠自动化可乐勿动",
                    "skuOrStoreCode": "coke",
                    "batchManage": 0,
                    "skuTypeStr": "销售品",
                    "shelfLife": 0,
                    "key": "581594449823932681",
                    "pictObj": {
                        "imageUrl": "https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png",
                        "iconType": ""
                    },
                    "titlePictObj": {
                        "imageUrl": "https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png",
                        "iconType": "",
                        "title": "肥肠自动化可乐勿动"
                    },
                    "costPrice": "2.00",
                    "pictUrl": "https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png",
                    "tagPrice": "3.00",
                    "rootCategoryId": "579422513618493721",
                    "outerId": "coke",
                    "rootCategoryName": "一级分类",
                    "leafCategoryId": "579422621789594490",
                    "categoryId": "579422513618493721",
                    "_id_": "itemId-{}".format(RandomUtils.random_str(7)),
                    "auxiliaryQuantity": qty,
                    "auxiliaryUnit": "瓶",
                    "relationNum": 1,
                    "basicQuantity": 2,
                    "actualUnitPrice": "3.0000",
                    "actualTotalPrice": "6.00",
                    "originalTotalAmount": "6.00",
                    "discountRate": "100",
                    "discountPrice": "0",
                    "includeTax": True,
                    "taxFee": "0.23",
                    "_id": 0,
                    "batchDisabled": True,
                    "batchPlaceholder": "未开启批次",
                    "inventoryAvailable": 4766,
                    "isGift": False,
                    "isCombined": False,
                    "picUrl": "https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png",
                    "scItemCode": "coke",
                    "scItemName": "肥肠自动化可乐勿动",
                    "scItemSkuName": "coke",
                    "scItemSkuCode": "coke",
                    "originUnitPrice": "3.00",
                    "auxiliaryUnitId": "576153968434971902",
                    "basicUnit": "瓶",
                    "brand": "测测测"
                }
            ],
            "discountRate": "100.00",
            "amountAfterDiscount": "6.00",
            "discountAmount": "0.00",
            "warehouseId": "1000100393",
            "warehouseName": "yubaby(yubaby)"
        }

        print("===> Order create request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> Order create success:{}".format(res))
        return {
            "channelOrderId": res["result"]["executeSucceed"][0]
        }

    def search(self, channelOrderIds = "", ):
        url = "https://omssaas-sit.zacz.cn/api/erp_order/order_search"
        data = {
            "limit": 30,
            "start": 0,
            "batchOrderId": "",
            "orderStatusList": [],
            "abTags": [],
            "isQuery": True,
            "channelOrderIds": channelOrderIds,
            "showCombo": True
        }
        print("===> Order search request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> Order search success:{}".format(res))

        targetList = []
        for item in res["result"]:
            targetList.append({
                "batchOrderId": item["batchOrderId"],
                "fulfillmentOrderIds": item["fulfillmentOrderIds"],
                "merchantId": item["merchantId"],
                "subDistributionOrderId": "subDistributionOrderId" in item and item["subDistributionOrderId"] or None
            })
        return targetList

    def auditOrder(self, commands):
        url = "https://omssaas-sit.zacz.cn/api/erp_order/batch_audit_order"
        data = {
            "commands": commands
        }
        print("===> Order audit request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> Order audit success:{}".format(res))
        return res

    def searchDistribution(self, channelOrderIds):
        url = "https://omssaas-sit.zacz.cn/api/erp_ship/queryDistributionOrderList"
        data = {
            "channelOrderIds": channelOrderIds,
            "isQuery": True,
            "limit": 200,
            "start": 0,
            "_fields": []
        }
        print("===> Distribution search request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> Distribution search response:{}".format(res))
        return res["result"]

    def batchOutBound(self, distributionOrders):
        url = "https://omssaas-sit.zacz.cn/api/erp_ship/batchOutBound"
        data = {
            "selected" : distributionOrders,
            "shipType": "ManualPrint",
            "shipType1": "manual"
        }
        print("===> BatchOutBound request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> BatchOutBound response:{}".format(res))

    def createReverseOrderDemo(self):
        url = "https://omssaas-sit.zacz.cn/api/erp_reverse/save_reverse_order"
        data = {"type":"5","customer":{},"store":{"value":"1000000004022925","label":"yubaby"},"applyTime":"2023-12-26 16:47:22","salesBiz":{"value":"retail","label":"零售业务"},"refundAmount":600,"refundPostAmount":0,"actualRefundAmount":600,"customerName":"","reverseType":1,"exchangeAmount":0,"bizSource":"","batchOrderIds":["4012336020620214"],"tradeOrderId":"930000026430614","returnLines":[{"outSubOrderType":1,"gift":0,"refundBasicUnit":"瓶","lineIndex":"2112336027316218","volumn":"0","refundUnitId":"576153968434971902","features":{"inputVText":"coke","apply_refund_quantity":"0","discountRate":"100","discountFee":"0","combPostFee":"0","shouldPayFee":"600","salesPrice":"300","wtRatio":"1000000000","unitFee":"300","unitTotalFee":"600","sharedShippingFee":"0","scItemSkuTypes":"0","auxiliaryUnitId":"576153968434971902","auxiliaryUnit":"瓶","auxiliaryUnitPrice":"30000","merchantId":"3592","supplierTradeOrderLineId":"930000026430621","supplierSkuCode":"coke","purchasePostFee":"0","brand":"测测测","scItemSkuCode":"coke","afterSaleTag":"200","scItemProperty":"coke","sendQuantity":"0","scItemId":"581594449823932681","scItemPic":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","dealTotalFee":"600","combActualFee":"0","taxRate":"4","combShouldPayFee":"0","dealUnitFee":"30000","brandId":"579424657875751047","lengthUnit":"cm","relationNum":"1","brandNameCn":"测测测","combDealTotalFee":"0","weightUnit":"kg","basicUnitId":"576153968434971902","apply_refund_fee":"600","supplierId":"202203232344300251","discountPrice":"0","actualPaidFee":"600","combUnitTotalFee":"0","supplierShipOrderDetailsIds":"2112336027316224","basicQuantity":"10000","platformPromotion":"0","scItemName":"肥肠自动化可乐勿动","scItemUnit":"瓶","taxFee":"23","deliveryDate":"1703580358000","channelOrderId":"SO231226000000090","supplierName":"零售云SAAS测试公司","comboNotSplited":"0","oltags":"normal","printedLogistics":"0","scItemCode":"coke","fulfillOrderDetailId":"1112336024968198","costPrice":"200","postFee":"0","fastPreShip":"0","vlRatio":"10000","basicUnit":"瓶","fulfillTag":"100","rootCategoryId":"579422513618493721","includeTax":"true","combPlatformPromotion":"0","supplierSkuName":"肥肠自动化可乐勿动","printedShipment":"0","scItemUnitId":"576153968434971902","combDiscountFee":"0","wmsLogisticsList":"[{\"appendPack\":false,\"childWaybill\":false,\"expressCode\":\"SFCSKpWICb9H\",\"isEditHidden\":true,\"logisticsCompanyCode\":\"SF\",\"logisticsCompanyName\":\"顺丰速运\",\"normalWaybill\":false,\"parentWaybill\":false,\"sendGoods\":false,\"writeRemark\":false}]","leafCategoryId":"579422621789594490","fulfillOrderId":"1012336021054198","purchaseUnitFee":"15000"},"picUrl":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","fulfillmentBatchId":4012336020620214,"merchantId":"3592","refundBasicUnitId":"576153968434971902","refundQuantity2B":"2","bizStatus":30,"brand":"测测测","refundUnit":"瓶","scItemSpecs":[{"specType":1,"scItemType":0,"unitName":"瓶","scItemId":"581594449823932681","label":"瓶","unitId":"576153968434971902","relationNum":1,"value":"576153968434971902"}],"unitPrice":300,"syncVersion":14,"shipOrderDetailsCreateTime":"2023-12-26 16:45:34","scItemProperty":"coke","mainStatus":"all_shipped","defectiveGoodsQuantity":0,"sendQuantity":2,"outSubOrderId":"930000026430615","combo":0,"weight":"0","scItemId":"581594449823932681","totalAmount":600,"unit":"瓶","canApplyRefundQuantity":2,"fulfillmentOrderId":1012336021054198,"warehouseId":"","outOrderId":"930000026430614","applyRefundQuantity":0,"relationNum":1,"status":1,"shipOrderId":2012336021852214,"itemType":0,"skuProperty":"coke","skuName":"肥肠自动化可乐勿动","scItemName":"肥肠自动化可乐勿动","refunded":True,"shipStatus":"已发货","channelOrderId":"SO231226000000090","actualReturnQuantity":0,"quantity":2,"scItemCode":"coke","includeTax":True,"fulfillmentOrderDetailId":1112336024968198,"tenantId":"202312051101032138","shipOrderDetailsId":2112336027316218,"__rowIndex":0}],"exchangeLines":[],"imageUrls":[],"salesBusinessName":"零售业务","salesBusiness":"retail","storeId":"1000000004022925","storeName":"yubaby","returnAddress":{},"receiverAddress":None};
        print("===> CreateReverseOrderDemo request:{}".format(data))
        res = requests.post(url=url, headers=self.headers, cookies=self.cookies, data=json.dumps(data)).json()
        print("===> CreateReverseOrderDemo response:{}".format(res))

if __name__ == '__main__':
    disOrderHandle = Order("18729884399", "lingyang666")
    # for i in range(500):
    #     disOrderHandle.createReverseOrderDemo()
    channelOrderIds = []
    for i in range(5):
        order = disOrderHandle.create(qty=10)
        channelOrderIds.append(order["channelOrderId"])
    time.sleep(5)
    shipOrders = disOrderHandle.search(",".join(channelOrderIds))
    disOrderHandle.auditOrder(shipOrders)
    time.sleep(10)
    subDistributionOrderIds = [item["subDistributionOrderId"] for item in disOrderHandle.search(",".join(channelOrderIds))]
    print("===> subDistributionOrderIds:{}".format(subDistributionOrderIds))


    supOrderHandle = Order("15663441700", "lingyang666")
    supShipOrders = supOrderHandle.search(",".join(subDistributionOrderIds))
    supOrderHandle.auditOrder(supShipOrders)
    time.sleep(2)
    distributionOrders = supOrderHandle.searchDistribution(",".join(subDistributionOrderIds))
    for result in distributionOrders:
        result["wmsLogisticsSDO"] = {
            "expressCode": "SF{}".format(RandomUtils.random_str(10)),
            "expressConfigCode": "SF",
            "expressConfigName": "顺丰速运",
            "logisticsCompanyCode": "SF",
            "logisticsCompanyName": "顺丰速运"
        }
    supOrderHandle.batchOutBound(distributionOrders)





