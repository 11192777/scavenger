/**
 * Created by jiachenpan on 16/11/18.
 */
export default {
  isvalidUsername(str) {
    return true
  },
  validateURL(textval) {
    const urlregex = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/
    return urlregex.test(textval)
  },
  validateLowerCase(str) {
    const reg = /^[a-z]+$/
    return reg.test(str)
  },
  validateUpperCase(str) {
    const reg = /^[A-Z]+$/
    return reg.test(str)
  },
  validatAlphabets(str) {
    const reg = /^[A-Za-z]+$/
    return reg.test(str)
  },
  validateDouble(number) {
    const re = /^\d+(.\d+)?$/
    return re.test(number)
  }

}

