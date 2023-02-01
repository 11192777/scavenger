<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="sqlAdapterOperator" placeholder="类型" class="filter-item" style="margin-left: 1%;">
        <el-option v-for="item in sqlAdapterSelectorItems" :key="item" :label="item" :value="item"/>
      </el-select>
      <el-button v-waves class="filter-item" type="primary" @click="execute" icon="el-icon-caret-right" style="margin-left: 1%;">执行</el-button>
    </div>
    <el-row class="demo-autocomplete" style="margin-top: 10px;">
      <el-col :span="12" style="width: 47%; margin-left: 1%;">
        <el-input type="textarea" wrap="off" :autosize="{ minRows: 15}" placeholder="请输入内容" v-model="inputArea"></el-input>
      </el-col>
      <el-col :span="12" style="width: 47%; margin-left: 2%;">
        <el-input type="textarea" wrap="off" :autosize="{ minRows: 15}" v-model="outputArea"></el-input>
      </el-col>
    </el-row>
    <br>
    <br>
  </div>
</template>

<script>
import SqlAdapterApi from '@/api/sqlAdapter'
import waves from '@/directive/waves'
import {parseTime} from '@/utils/temp'
import Pagination from '@/components/Pagination'

const calendarTypeOptions = [
  {key: 'CN', display_name: 'China'}
]

// arr to obj ,such as { CN : "China", US : "USA" }
const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {
  name: 'ComplexTable',
  directives: {waves},
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
    }
  },
  data() {
    return {
      sqlAdapterOperator: null,
      sqlAdapterSelectorItems: null,
      calendarTypeOptions,
      dialogFormVisible: false,
      dialogStatus: '',
      inputArea: null,
      outputArea: null
    }
  },
  created() {
    this.getSqlAdapterSelector()
  },
  methods: {
    getSqlAdapterSelector() {
      SqlAdapterApi.sqlAdapterSelector().then(res => {
        this.sqlAdapterSelectorItems = res
        this.sqlAdapterOperator = res[0]
      })
    },
    execute() {
      SqlAdapterApi.execute(this.sqlAdapterOperator, this.inputArea).then(res => {
        this.outputArea = res
      })
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    }
  }
}
</script>
