import request from '@/utils/request'

export default {

  fieldTemplateSelector() {
    return request({
      url: '/api/field_template/selector',
      method: 'get',
    })
  },

  execute(operator, content) {
    return request({
      url: '/api/field_template/execute',
      headers: {"Content-Type": "application/json"},
      method: 'post',
      params: {type: operator},
      data: content
    })
  }
}
