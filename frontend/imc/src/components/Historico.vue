<template>
    <div class="hist-bloco">
        <div class="row">
            <div class="column" @click="show_()">
                <div class="title">
                    <h5>{{ nome }}</h5>
                </div>   
            </div>
        </div>
        <div class="row" :id="id_paciente"  >   
            <div class="column">
                <div :id="'chart'+id_paciente" class="chart"  v-show="show"></div>
            </div>
        </div>
    </div>
</template>

<script>
var echarts = require('echarts');

export default {
  data(){
      return{
          chartDom:document.getElementById(String('chart'+this.id_paciente)),
          show:false
      }
  },
  methods:{
      show_:function(){
        this.show =! this.show; 
        this.resizeHandler()
      },
      resizeHandler:function() {
            var chartDom = document.getElementById(String('chart'+this.id_paciente));
            var myChart = echarts.init(chartDom);
            setTimeout(function(){
                myChart.resize();
            },3)
        }
  },
  created()  {
    window.addEventListener("resize", this.resizeHandler);
    },

    unmounted(){
        window.removeEventListener("resize", this.resizeHandler);
    },
    mounted(){
        var chartDom = document.getElementById(String('chart'+this.id_paciente));
        var myChart = echarts.init(chartDom);
        var option;

        option = {
            legend:{},
            tooltip: {},
            dataset:{
                dimensions: ['data','idade', 'peso', 'altura', 'imc'],
                source:this.historico
            },
        xAxis: {
            type: 'category'
        },
        yAxis: {},
        series: [{type:'line'},{type:'line'},{type:'line'},{type:'line'}]
        };

        option && myChart.setOption(option);
        
  },
  props:{
    id_paciente:Number,
    nome:String,
    historico:Object,

  }
}
</script>

<style>
.chart{
    height: 400px;
    width: 100%;
    resize: none;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

h5{
    display: flex;
}
</style>