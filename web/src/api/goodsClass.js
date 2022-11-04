import request from '@/utils/request'


export default {

  getGoodsClassList(listQuery) {
    return request({
      url: '/api/v1/goods/class/list',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createGoodsClass(foodGoodsClass){
    return request({
      url: '/api/v1/goods/class',
      method: 'post',
      data: foodGoodsClass
    })
  },
  updateData(formData){
    return request({
      url: '/api/v1/goods/class',
      method: 'put',
      data: formData
    })
  }
}
