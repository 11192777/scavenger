import request from '@/utils/request'

export default {

  sqlAdapterSelector() {
    return request({
      url: '/api/sql_adapter/selector',
      method: 'get',
    })
  },

  execute(operator, content) {
    return request({
      url: '/api/sql_adapter/execute',
      headers: {"Content-Type": "application/json"},
      method: 'post',
      params: {type: operator},
      data: content
    })
  }
}
