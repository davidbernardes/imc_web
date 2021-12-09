<template>
  <div class="conteiner">
    <div class="row">
      <div class="column column-50 column-offset-25">
        <!-- Calculadora IMC -->
        <form>
          <fieldset>
            <h3>Calculadora de Índice de Massa Corporal</h3>
            <hr>
            <div class="row">
              <div class="column column-75">
                <input type="text" name="nome" id="nome" placeholder="Nome do Pasciente" v-model="dados.nome">
              </div>
              <div class="column column-25">
                <input type="number" name="idade" id="idade" placeholder="Idade" v-model="dados.idade">
              </div>
            </div>
            <input type="text" name="endareco" id="endereco" placeholder="Endereço Completo" v-model="dados.endereco">
            <div class="row">
              <div class="column column-50">
                <input type="number" name="altura" id="altura" placeholder="Altura em cm. Ex: 170" v-model="dados.altura">
              </div>
              <div class="column column-50">
                <input type="number" name="peso" id="peso" placeholder="Peso em Kg. Ex: 80" v-model="dados.peso">
              </div>
            </div>
            <blockquote>
              <p><em><span id="resultado">{{ resultado() }}</span></em></p>
            </blockquote>
            <div class="float-right">
              <input type="submit" value="Salvar" class="button" @click="salvar()">
            </div>
          </fieldset>   
        </form>
        <!-- Histórico de Pacientes -->
        <hr>
        <div id="historico" class="row">
          <div class="column column-50">
            <h4>Histórico de Pacientes</h4>
          </div>
          <div class="column column-50">
            <input type="text" placeholder="Procurar" v-model="search">
          </div>
        </div>
        <div class="row hist-section">
          <div class="column ">
            <div v-for="(pasciente, index) in filteredItems" :key=pasciente>
              <hist :nome="pasciente.nome" :id_pasciente="index" :historico="pasciente.historico" />
            </div>
          </div> 
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'
import hist from '@/components/Historico.vue'

export default {
  name: 'App',
  components: {
    hist
  }, 
  data(){
    return {
      dados:{
        nome:"",
        endereco:"",
        altura:"",
        peso:"",
        idade:"",
        imc:"",
      },
      pacientes: [],
      search:""
    }
  },
  computed: {
    filteredItems() {
      let items = [];
      items = this.pacientes.filter((item) => {
        var name = this.replaceSpecialChars(item.nome)
        var search_item = this.replaceSpecialChars(this.search)

        return (
          name.indexOf(search_item) > -1
        );
      });
    return items;
    }
  },
  created(){
    api.get(pacientes =>{
      //console.log(pacientes);
      this.pacientes = pacientes;
    });
  },
  methods:{
    salvar:function(){
      if (this.validar_dados()){
        api.send(this.dados).then(
          resp => alert(resp.status)
        )
      }
      else{
        alert('Preencha Todos os Campos');
      }
    },
    validar_dados:function(){
      if(this.dados.altura && this.dados.peso && this.dados.nome && this.dados.endereco && this.dados.idade){
        return true   
      }
      return false
    },
    replaceSpecialChars:function(str){
      if (!str) return ''
      str = str.toLowerCase()
      str = str.replace(/[aáàãäâ]/,'a')
      str = str.replace(/[eéèëê]/,'e')
      str = str.replace(/[iíìïî]/,'i')
      str = str.replace(/[oóòõöô]/,'o')
      str = str.replace(/[uúùüû]/,'u')
      return str
    },
    resultado:function(){
      var altura = this.dados.altura/100;
      if (this.validar_dados()){
        this.dados.imc = this.dados.peso/altura**2
        return this.dados.imc.toFixed(2)+' '+this.classificacao(this.dados.imc)
      }
      else{
        return "Resultado"
      }
    },
    classificacao:function(imc){
      if (imc<18.5){
        document.getElementById('resultado').style.color = '#836FFF';
        return "Magreza"
      }
      if (imc>=18.5 && imc<=24.99){
        document.getElementById('resultado').style.color = '#00BFFF';
        return "Normal"
      }
      if (imc>=25 && imc<=29.99){
        document.getElementById('resultado').style.color = '#DAA520';
        return "Sobrepeso"
      }
      if (imc>=30 && imc<=39.99){
        document.getElementById('resultado').style.color = '#FF7F50';
        return "Obesidade"
      }
      if (imc>=40){
        document.getElementById('resultado').style.color = '#B22222';
        return "Obesidade Grave"
      }
    }
  }
}
</script>

<style>
#app{
  margin-top: 5em;
  max-width: 1900px;
  margin-left: auto;
  margin-right: auto;
}
.hist-section{
  margin-top: 50px;
}

</style>
