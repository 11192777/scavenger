import request from '@/utils/request'
import de from 'element-ui/src/locale/lang/de'


export default {

  getPositionList(listQuery) {
    return request({
      url: '/api/v1/department/positions',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createPosition(position){
    return request({
      url: '/api/v1/position',
      method: 'post',
      data: position
    })
  },

  updateData(formData){
    return request({
      url: '/api/v1/position',
      method: 'put',
      data: formData
    })
  }
}
