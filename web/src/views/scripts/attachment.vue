<template>
  <div class="components-container">
    <div class="editor-container">
      <dropzone id="myVueDropzone" url="https://httpbin.org/post" @dropzone-removedFile="dropzoneR" @dropzone-success="dropzoneS"/>
    </div>
  </div>
</template>

<script>
import Dropzone from '@/components/Dropzone'
import AttachmentApi from '@/api/attachment'
import GoodsAttachmentApi from '@/api/goodsAttachment'

export default {
  name: 'DropzoneDemo',
  components: { Dropzone },
  data(){
    return {

    }
  },
  methods: {
    dropzoneS(file) {
      const formData = new FormData()
      formData.append('file', file)
      AttachmentApi.uploadFile(formData).then(response => {

        GoodsAttachmentApi.goodsAttachment(this.$route.params.id, response.data.id).then(res =>{
          this.$notify({
            title: '上传成功',
            message: '创建成功',
            type: 'success',
            duration: 1000
          })
        })
      })
    },
    dropzoneR(file) {
      this.$message({ message: 'Delete success', type: 'success' })
    }
  }
}
</script>

