import request from '@/utils/request'


export default {

  getStaffList(listQuery) {
    return request({
      url: '/api/v1/staffs',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit
      }
    })
  },

  createStaff(staff){
    return request({
      url: '/api/v1/staff',
      method: 'post',
      data: staff
    })
  },
  deleteStaff(id){
    return request({
      url: '/api/v1/staff',
      method: 'delete',
      params:{
        id: id
      }
    })
  },
  updateData(formData){
    return request({
      url: '/api/v1/staff',
      method: 'put',
      data: formData
    })
  }
}
