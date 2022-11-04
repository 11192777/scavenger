import request from '@/utils/request'


export default {

  getSiteList(type) {
    return request({
      url: '/api/v1/sites',
      method: 'get',
      params: {
        type: type
      }
    })
  },
  getSiteByParentId(parentId){
    return request({
      url: '/api/v1/sites/by/parentId',
      method: 'get',
      params: {
        parentId: parentId
      }
    })
  }
}
