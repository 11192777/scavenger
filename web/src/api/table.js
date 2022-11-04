import request from '@/utils/request'

export function getList(listQuery) {
  return request({
    url: `/table/list?id=${listQuery.page},size=${listQuery.size}`,
    method: 'get',
  })
}
