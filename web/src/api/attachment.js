import request from '@/utils/request'

export default {

  uploadFile(file) {
    return request({
      url: '/api/attachment/upload',
      method: 'post',
      headers: {
        'Content-Type': 'multipart/form-data; charset=utf-8'
      },
      data: file
    })
  }
}
