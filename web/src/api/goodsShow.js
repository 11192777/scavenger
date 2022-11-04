import request from '@/utils/request'


export default {

  getGoodsShowList(listQuery) {
    return request({
      url: '/api/v1/goods/shows',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createGoodsShow(goodsShow){
    return request({
      url: '/api/v1/goods/show',
      method: 'post',
      data: goodsShow
    })
  }
}
