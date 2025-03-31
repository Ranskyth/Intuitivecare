<template>
  <main>
    <div class="container">
      <input v-model="valor" placeholder="Valor" />
      <input v-model="coluna" placeholder="Coluna" />
      <button @click="submitSearch">Search</button>
  
      <div v-if="result.length">
        <div v-for="(row, index) in result" :key="index" class="row">
          <div v-for="(value, key) in row" :key="key">
            <span v-if="key !== 'long_text_key'">{{ key }}: {{ value }}</span>
          </div>
        </div>
      </div>
      <p v-else>No results found</p>
    </div>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      valor: '',
      coluna: '',
      result: []
    }
  },
  methods: {
    async submitSearch() {
      if (!this.valor || !this.coluna) return alert("valor ou coluna vazio")

      try {
        const { data } = await axios.post('http://127.0.0.1:8000/buscar', {
          valor: this.valor,
          coluna: this.coluna
        })
        this.result = typeof data === 'string' ? JSON.parse(data) : data
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 450px;
  justify-self: center;
}
main{
  margin: auto;
}
input{
  padding: 10px;
  width: 450px;
}
.row {
  padding: 5px;
  border-bottom: 1px solid #ddd;
}
button{
  padding: 10px;
}
</style>
