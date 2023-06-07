<template>
  <div>
    <button @click="getData()">获取api数据</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      msg: "主页"
    }
  },
  methods:{
   getData(){
      var api="https://apiv3.shanbay.com/weapps/dailyquote/quote/";
      axios.get(api).then((res)=>{
        console.log(res)
      }).catch((err)=>{
        console.log(err)
      })
   }

  }
};
</script>