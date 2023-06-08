<template>
 <div class='Card'>
  <div style="display: grid;grid-template-columns: 33.33% 33.33% 33.33%;">
      <div v-for="it in data_target">
        <div class="卡片">
        <div class="内容">
          <div class="图框">
            <img class="预览图" :src="it.pic" style="background-size: contain;" referrerPolicy="no-referrer" />
          </div>
          <div class="信息">
            <a :href="it.url" target="_blank" :title='it.title'>{{it.title}}</a>
            <span><i class="far fa-id-card" /> {{it.author}}</span>
            <span><i class="far fa-calendar" /> {{times(it.pubdate)}}</span>
            <div style="display: flex;padding: 0 5% 0 0;justify-content: space-between;">
              <span><i class="fa fa-play" /> {{it.play}}</span>
              <span><i class="far fa-star" /> {{it.favorites}}</span>
              <span><i class="far fa-clock" /> {{it.duration}}</span>
            </div>
          </div>
        </div>
        </div>
      </div>
  </div>
 </div>
</template>

<script>
import data from './public/data.json'

export default {
  props:{
    "target":{type:String,default:'cookie'}
  },
  data() {
    return {
      jsonData: data
    }
  },
  computed:{
    // 在data中获取符合target的列表
    data_target(){
      let jd = this.jsonData;
      for(let i in jd){
        if (jd[i][this.target] != undefined)
          return jd[i][this.target];
      }
    },
  },
  methods:{
    times(t){
      let now = new Date(parseInt(t) * 1000);
      return now.toLocaleString('chinese',{hour12:false});
    }
  }
}
</script>

<style type="text/css">
:root {
--背景颜色: var(--vp-custom-block-tip-bg);
/*--卡片默认颜色: #3f4047;
--卡片默认颜色2: #ed4845;//淡菽红
--卡片纹理: rgba(0, 0, 0, 0.2);*/
--图片背景: rgba(0, 0, 0, 0.08);
--图片边框: rgba(0, 0, 0, 0.08);
--字体颜色: var(--vp-c-text-2);
--卡片边缘: rgba(212,205,150,0.6);
--卡片悬停: rgba(255,255,255,1);
--动画时间: 0.13s;
}
.Card {
  font-family: "Monaco", "Consolas", "Liberation Mono", monospace;
  padding: 1em 0em;
  width: 100%;
  height: 100vh;
  overflow-y: scroll;
}
.卡片 {
  position: relative;
  background: var(--背景颜色);
  height: 16em;
  margin: 5px;
  transition: transform var(--动画时间) ease-in-out;
  .内容 {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: repeating-linear-gradient(135deg, var(--卡片纹理), transparent 2px, var(--卡片纹理) 3px);
    border: 1px var(--卡片边缘) solid;
    border-radius: 9px;
    background-color: var(--卡片默认颜色);
    box-shadow: 4px 4px 15px rgba(0,0,0,0.4);

    .信息 {
      display: block;
      flex-wrap: wrap;
      justify-content: center;
      position: absolute;
      bottom: 0.2em;
      width: 100%;
      
    }
    .信息 span {
      display: block;
      font-size: 12px;
      color: var(--字体颜色);
      margin-left: 1em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .信息 a {
      display: block;
      font-weight: bolder;
      font-size: 12px;
      color: #66aadb;
      margin-left: 1em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .图框 {
      position: absolute;
      top: 32.5%;
      left: 50%;
      width: 45%;
      border: 0px var(--图片边框) solid;
      transform: translate(-50%, -50%);
      z-index: 1;
      background:
        linear-gradient(to right, var(--字体颜色) 1px, transparent 1px) 0 0,
        linear-gradient(to right, var(--字体颜色) 1px, transparent 1px) 0 100%,
        linear-gradient(to left, var(--字体颜色) 1px, transparent 1px) 100% 0,
        linear-gradient(to left, var(--字体颜色) 1px, transparent 1px) 100% 100%,
        linear-gradient(to bottom, var(--字体颜色) 1px, transparent 1px) 0 0,
        linear-gradient(to bottom, var(--字体颜色) 1px, transparent 1px) 100% 0,
        linear-gradient(to top, var(--字体颜色) 1px, transparent 1px) 0 100%,
        linear-gradient(to top, var(--字体颜色) 1px, transparent 1px) 100% 100%;
      background-repeat: no-repeat;
      background-size: 12px 12px;
      background-color: var(--图片背景);
      user-select: none;/*禁止选择*/
    }
    .预览图 {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(2);
      z-index: 1;
    }

  }
}

.卡片:hover {
  transform: translate(-0%, -5%) scale(1.02);
  box-shadow: 0 0 0 2px var(--卡片悬停);
  border-radius: 10px;
  transition: transform var(--动画时间) ease-in-out;
  z-index: 100
}
</style>