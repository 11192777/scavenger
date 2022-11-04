import request from '@/utils/request'

export default {

  getMarketList(listQuery) {
    return request({
      url: '/api/v1/markets',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createMarket(market) {
    return request({
      url: '/api/v1/market',
      method: 'post',
      data: market
    })
  },
  updateMarket(id, status) {
    return request({
      url: '/api/v1/market/status',
      method: 'put',
      params: {
        id: id,
        status: status
      }
    })
  },
  updateData(formData){
    return request({
      url: '/api/v1/market',
      method: 'put',
      data: formData
    })
  }
}
