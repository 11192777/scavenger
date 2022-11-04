import request from '@/utils/request'


export default {

  getGoodsRepositoryList(listQuery) {
    return request({
      url: '/api/v1/goods/repositorys',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createGoodsRepository(goodsRepository){
    return request({
      url: '/api/v1/goods/repository',
      method: 'post',
      data: goodsRepository
    })
  },

  updateData(formData){
    return request({
      url: '/api/v1/goods/repository',
      method: 'put',
      data: formData
    })
  }
}
