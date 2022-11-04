import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: '/api/wechat/user/login',
    method: 'post',
    data:{
      username: username,
      password: password
    }
  })
}

export function getInfo() {
  return request({
    url: '/api/v1/token',
    method: 'get',
  })
}

export function logout() {
  return request({
    url: '/user/logout',
    method: 'post'
  })
}
