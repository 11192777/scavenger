import request from '@/utils/request'

export default {

  goodsAttachment(goodsId, attachmentId) {
    return request({
      url: '/api/v1/goods/attachment',
      method: 'post',
      data: {
        goodsId: goodsId,
        attachmentId: attachmentId
      }
    })
  }
}
