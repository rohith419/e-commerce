<template>
  <div class="p-4">
    <h2>Products</h2>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div v-for="p in products" :key="p.id" style="border:1px solid #ddd; padding:8px; margin:8px 0;">
        <h3>{{ p.title }} — ₹{{ p.price }}</h3>
        <p>{{ p.description }}</p>
        <router-link :to="`/product/${p.id}`">View</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  data(){ return { products: [], loading: true } },
  async mounted(){
    try{
      const res = await axios.get('http://127.0.0.1:8000/api/products/')
      this.products = res.data
    }catch(e){ console.error(e) }
    this.loading = false
  }
}
</script>
