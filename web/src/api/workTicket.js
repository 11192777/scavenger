import request from '@/utils/request'

export default {

  workTicketSelector() {
    return request({
      url: '/api/work_ticket/selector',
      method: 'get',
    })
  },

  execute(operator, content) {
    return request({
      url: '/api/work_ticket/execute',
      headers: {"Content-Type": "application/json"},
      method: 'post',
      params: {type: operator},
      data: content
    })
  }
}
