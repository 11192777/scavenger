import request from '@/utils/request'

export default {

  strUtilSelector() {
    return request({
      url: '/api/str_util/selector',
      method: 'get',
    })
  },

  execute(operator, content) {
    return request({
      url: '/api/str_util/execute',
      headers: {"Content-Type": "application/json"},
      method: 'post',
      params: {type: operator},
      data: content
    })
  }
}
