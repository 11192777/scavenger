import request from '@/utils/request'


export default {

  getOrderList(listQuery) {
    return request({
      url: '/api/v1/orders',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  }
}
