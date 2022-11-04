import request from '@/utils/request'


export default {

  getCourierList(listQuery) {
    return request({
      url: '/api/v1/couriers',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createCourier(courier){
    return request({
      url: '/api/v1/courier',
      method: 'post',
      data: courier
    })
  },

  updateData(formData){
    return request({
      url: '/api/v1/courier',
      method: 'put',
      data: formData
    })
  }
}
