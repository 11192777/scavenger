<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="sqlAdapterOperator" placeholder="类型" class="filter-item" style="width: 150px; margin-left: 1%;">
        <el-option v-for="item in sqlAdapterSelectorItems" :key="item" :label="item" :value="item"/>
      </el-select>
      <el-button v-waves class="filter-item" type="primary" @click="execute" icon="el-icon-caret-right" style="margin-left: 1%;">执行</el-button>
    </div>
    <el-form :model="info" label-position="left" label-width="150px" style="width: 400px; margin-left:50px; margin-top: 50px;">
      <el-form-item label="Words limit" prop="title">
        <el-input v-model="info.wordsLimit" />
      </el-form-item>
      <el-form-item label="Max words limit" prop="title">
        <el-input v-model="info.wordsMaxLimit" />
      </el-form-item>
      <el-form-item label="Item limit" prop="title">
        <el-input v-model="info.itemLimit" />
      </el-form-item>
      <el-form-item label="Max item limit" prop="title">
        <el-input v-model="info.itemMaxLimit" />
      </el-form-item>
      <el-form-item label="Tenant ID" prop="title">
        <el-input v-model="info.tenantId" />
      </el-form-item>
      <el-form-item label="Form codes" prop="title">
        <el-input v-model="info.formCodes" />
      </el-form-item>
      <el-form-item label="Field codes" prop="title">
        <el-input v-model="info.fieldCodes" />
      </el-form-item>
    </el-form>
    <el-row class="demo-autocomplete" style="margin-top: 10px;">
      <el-col :span="12" style="width: 47%; margin-left: 2%;">
        <el-input type="textarea" wrap="off" :autosize="{ minRows: 15}" v-model="outputArea"></el-input>
      </el-col>
    </el-row>
    <br>
    <br>
  </div>
</template>

<script>
import WorkTicketApi from '@/api/workTicket'
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
      outputArea: null,
      info: {
        wordsLimit: 100,
        wordsMaxLimit: 100,
        itemLimit: 100,
        itemMaxLimit: 100,
        tenantId: null,
        formCodes: null,
        fieldCodes: null,
      }
    }
  },
  created() {
    this.getWorkTicketSelector()
  },
  methods: {
    getWorkTicketSelector() {
      WorkTicketApi.workTicketSelector().then(res => {
        this.sqlAdapterSelectorItems = res
        this.sqlAdapterOperator = res[0]
      })
    },
    execute() {
      WorkTicketApi.execute(this.sqlAdapterOperator, this.info).then(res => {
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
