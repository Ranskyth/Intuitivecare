<template>
    <div>
      <input v-model="searchValue" placeholder="Search Value" />
      <input v-model="searchColumn" placeholder="Search Column" />
      <button @click="submitSearch">Search</button>
      <div v-for="(row, index) in result">
        <div v-for="(value, key) in Object.entries(row)" v-bind:key="key">
          <span v-if="key != 'long_text_key'">{{ key }}: {{ value }}</span>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        searchValue: '',
        searchColumn: '',
        result: []
      }
    },
    methods: {
      async submitSearch() {
        const data = {
          search_value: this.searchValue,
          search_column: this.searchColumn
        }
        try {
          const res = await axios.post('http://localhost:5000/submit', data)
          this.result = JSON.parse(res.data)
        } catch (err) {
          console.error(err)
        }
      }
    }
  }
  </script>