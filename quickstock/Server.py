import json

import requests
from requests.cookies import RequestsCookieJar

if __name__ == '__main__':
    data = {
        "loginType": 0,
        "password": "lingyang666",
        "account": "15663441700",
        "tenant": "202203232344300251",
        "product": "QuickStock",
        "goods": "erp_quickstock",
        "channel": None,
        "redirect_uri": ""
    }
    cookie = RequestsCookieJar()
    headers = {"Content-Type": "application/json", "linked_env_tag": "f2c74ef4"}
    response = requests.post("https://sit-auth.zacz.cn/api/doLogin", headers=headers, data=json.dumps(data), cookies=cookie)
    cookie.update(response.cookies)
    print(cookie.get("XSRF-TOKEN"))
    print(response.json())
    print(cookie.get("bizphin_auth_token"))

    cookie.set("bizphin_auth_token", cookie.get("bizphin_auth_center_token"))

    print("===>" + cookie.get("bizphin_auth_token"))

    headers["bizphin_auth_token"] = cookie.get("bizphin_auth_center_token")
    headers["x-xsrf-token"] = "456000c3-daf2-4822-ae1f-f199d0e8a642"
    print(headers)
    cooke = {"receiver":{"deliveryType":{"label":"快递配送","value":1},"name":"Mrna-me","contactNumber":"13777777777","harvestAddress":[{"childElements":[{"childElements":[{"code":"310107","name":"普陀区"}],"code":"310100","name":"上海市","next":{"code":"310107","name":"普陀区"}}],"code":"310000","name":"上海","next":{"childElements":[{"code":"310107","name":"普陀区"}],"code":"310100","name":"上海市","next":{"code":"310107","name":"普陀区"}}}],"detailAddress":"长风新村街道金沙江路1000号","deliveryTypeId":1,"deliveryTypeName":"快递配送","provinceCode":"310000","province":"上海","cityCode":"310100","city":"上海市","districtCode":"310107","district":"普陀区"},"organizationInfo":{},"invoice":{"open":False},"salesBusiness":"retail","orderType":"normal","orderFrom":"manualCreate","extCreateTime":"2023-12-20 11:26:36","postFee":0,"totalDiscountFee":0,"actualTotalPrice":30,"shouldPayFee":30,"salesBusinessText":"零售业务","storeId":"1000000004022925","warehouse":{"deep":0,"value":"1000100393","label":"yubaby(yubaby)","code":"yubaby","type":3,"features":{"enableNegative":"0"},"model":1,"id":"1000100393","wmsType":"0","name":"yubaby","status":1},"addressTool":"长风新村街道金沙江路1000号，13777777777，Mrna me","orderLines":[{"inputVText":"coke","salesPrice":"3.00","skuTypeList":[0],"type":0,"baseUnit":{"unitName":"瓶","scItemId":"581594449823932681","label":"瓶","unitId":"576153968434971902","relationNum":1,"value":"576153968434971902"},"itemName":"肥肠自动化可乐勿动","virtualStr":"否","merchantId":"3592","price":"3.00","id":"581594449823932681","brandName":"测测测","unitName":"瓶","scItemId":"581594449823932681","tags":[],"taxRate":"4","itemId":"581594449823932681","brandId":"579424657875751047","skuCode":"coke","status":1,"basicUnitId":"576153968434971902","virtual":0,"scItemSpecList":[{"unitName":"瓶","scItemId":"581594449823932681","label":"瓶","unitId":"576153968434971902","relationNum":1,"value":"576153968434971902"}],"code":"coke","itemProperty":"coke","title":"肥肠自动化可乐勿动","skuOrStoreCode":"coke","batchManage":0,"skuTypeStr":"销售品","shelfLife":0,"key":"581594449823932681","pictObj":{"imageUrl":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","iconType":""},"titlePictObj":{"imageUrl":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","iconType":"","title":"肥肠自动化可乐勿动"},"costPrice":"2.00","pictUrl":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","tagPrice":"3.00","rootCategoryId":"579422513618493721","rootCategoryName":"一级分类","outerId":"coke","leafCategoryId":"579422621789594490","categoryId":"579422513618493721","_id_":"itemId-lmpUXQVj","auxiliaryQuantity":"10","auxiliaryUnit":"瓶","relationNum":1,"basicQuantity":"10","actualUnitPrice":"3.0000","actualTotalPrice":"30.00","originalTotalAmount":"30.00","discountRate":"100","discountPrice":"0.00","includeTax":True,"taxFee":"1.15","_id":0,"batchDisabled":True,"batchPlaceholder":"未开启批次","inventoryAvailable":5000,"isGift":False,"isCombined":False,"picUrl":"https://tn01-image-sit-jushita.zacz.cn/omssaas/202312051101032138/item/itemImage/20231220/0cd4b99ecfb15e041148d1f5d3e0e630.png?originName=Snipaste_2023-12-20_111754.png","scItemCode":"coke","scItemName":"肥肠自动化可乐勿动","scItemSkuName":"coke","scItemSkuCode":"coke","originUnitPrice":"3.00","auxiliaryUnitId":"576153968434971902","basicUnit":"瓶","brand":"测测测"}],"discountRate":"100.00","amountAfterDiscount":"30.00","discountAmount":"0.00","warehouseId":"1000100393","warehouseName":"yubaby(yubaby)"}
    res = requests.post("https://omssaas-sit.zacz.cn/api/erp_order/create_order_api", headers=headers, data=json.dumps(cooke), cookies=cookie).json()
    print(res)

    if (res["errorMessage"])
        headers[""]