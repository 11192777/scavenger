<template>
  <div class="app-container">

    <div class="filter-container">
      <el-input :placeholder="'标题'" v-model="listQuery.title" style="width: 200px;" class="filter-item"/>
      <el-select v-model="listQuery.type" :placeholder="'类型'" clearable class="filter-item" style="width: 230px">
        <el-option v-for="item in calendarTypeOptions" :key="item.key" :label="item.display_name+'('+item.key+')'" :value="item.key"/>
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search">搜索</el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">添加</el-button>
    </div>
    <br>
    <br>
    <el-table
      v-loading="listLoading"
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange">
      <el-table-column label="序号" width="70" align="center">
        <template slot-scope="scope">
          {{ (listQuery.page - 1) * listQuery.limit + scope.$index + 1 }}
        </template>
      </el-table-column>
      <el-table-column :label="'分类名称'" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.value }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="'分类编码'" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.key }}</span>
        </template>
      </el-table-column>

      <el-table-column :label="'操作'" align="center" width="120" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList"/>

<!--  新增编辑界面  -->
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="this.goodsClassEntity" label-position="left" label-width="100px" style="width: 400px; margin-left:50px;">
        <el-form-item :label="'分类名称'">
          <el-input v-model="goodsClassEntity.name"/>
        </el-form-item>
        <el-form-item :label="'分类编码'">
          <el-input v-model="goodsClassEntity.code"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" v-if="dialogStatus == 'create'" @click="createData()">确定</el-button>
        <el-button type="primary" v-if="dialogStatus == 'update'" @click="updateData()">确定</el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel"/>
        <el-table-column prop="pv" label="Pv"/>
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">确定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
import MarketApi from '@/api/market'
import waves from '@/directive/waves' // Waves directive
import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
import Util from '@/utils/validate'
import GoodsClassApi from '@/api/goodsClass'

const calendarTypeOptions = [
  { key: 'CN', display_name: 'China' }
]

const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {

  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
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
      tableKey: 0,
      list: null,
      marketList: null,
      positionList: null,
      total: 0,
      listLoading: true,
      goodsClassEntity:{
        id: null,
        name: null,
        code: null
      },
      listQuery: {
        page: 1,
        limit: 20,
        importance: undefined,
        title: undefined,
        type: undefined
      },
      radio: true,
      importanceOptions: [1, 2, 3],
      calendarTypeOptions,
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['published', 'draft', 'deleted'],
      showReviewer: false,
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    cropSuccess(resData) {
      this.imagecropperShow = false
      this.imagecropperKey = this.imagecropperKey + 1
      this.image = resData.files.avatar
    },
    close() {
      this.imagecropperShow = false
    },
    dropzoneS(file) {
      console.log(file)
      this.$message({ message: 'Upload success', type: 'success' })
    },
    dropzoneR(file) {
      console.log(file)
      this.$message({ message: 'Delete success', type: 'success' })
    },
    getMarketList(){
      MarketApi.getMarketList(this.listQuery).then(res =>{
        this.marketList = res.data
      })
    },
    getList() {
      this.listLoading = true
      setTimeout(() => {
        GoodsClassApi.getGoodsClassList(this.listQuery).then(response => {
          this.list = response.data
          this.total = response.total

          // Just to simulate the time of the request
          setTimeout(() => {
            this.listLoading = false
          })
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleModifyStatus(row, status) {
      this.goodsClassEntity.repositoryId = row.id
      this.temp = Object.assign({}, row) // copy obj
      this.temp.createData = new Date(this.temp.timestamp)
      this.dialogStatus = 'status'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.goodsClassEntity = {
        id: null,
        name: null,
        code: null
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      GoodsClassApi.createGoodsClass(this.goodsClassEntity).then(() =>{
        this.dialogFormVisible = false
        this.$notify({
          title: '成功',
          message: '创建成功',
          type: 'success',
          duration: 2000
        })
        this.getList()
      })
    },
    releaseData(){

      if (!Util.validateDouble(this.goodsClassEntity.price)){
        this.$notify({
          title: '错误',
          message: '请输入正确的价格',
          type: 'error',
          duration: 2000
        })
        return
      }

      GoodsClassApi.createGoodsClass(this.goodsClassEntity).then(() =>{
        this.dialogFormVisible = false
        this.$notify({
          title: '成功',
          message: '发布成功',
          type: 'success',
          duration: 2000
        })
        this.getList()
      })
    },
    handleUpdate(row) {
      this.goodsClassEntity.id = row.id
      this.goodsClassEntity.code = row.key
      this.goodsClassEntity.name = row.value
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          GoodsClassApi.updateData(this.goodsClassEntity).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getList()
          })
        }
      })
    },
    handleDelete(row) {
      this.$notify({
        title: '成功',
        message: '删除成功',
        type: 'success',
        duration: 2000
      })
      const index = this.list.indexOf(row)
      this.list.splice(index, 1)
    },
    handleFetchPv(pv) {
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
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
