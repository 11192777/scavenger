import request from '@/utils/request'


export default {

  getDepartmentList(listQuery, companyId) {
    return request({
      url: '/api/v1/departments',
      method: 'get',
      params: {
        page: listQuery == null ? null : listQuery.page,
        limit: listQuery == null ? null : listQuery.limit,
        companyId: companyId
      }
    })
  },

  createDepartment(department){
    return request({
      url: '/api/v1/department',
      method: 'post',
      data: department
    })
  },

  updateData(formData){
    return request({
      url: '/api/v1/department',
      method: 'put',
      data: formData
    })
  }
}
