<template>
  <div class="p-4">
    <div v-if="loading">Loading...</div>
    <div v-else-if="product">
      <h2>{{ product.title }}</h2>
      <p>{{ product.description }}</p>
      <p>Price: ₹{{ product.price }}</p>
      <button @click="addToCart">Add to cart</button>
    </div>
    <div v-else>Product not found.</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProductDetails',
  props: ['id'],
  data(){ return { product: null, loading: true } },
  async mounted(){
    try{
      const res = await axios.get(`http://127.0.0.1:8000/api/products/${this.$route.params.id}/`)
      this.product = res.data
    }catch(e){ console.error(e) }
    this.loading = false
  },
  methods:{
    addToCart(){
      const cart = JSON.parse(localStorage.getItem('cart')||'[]')
      cart.push({ product: this.product, quantity: 1 })
      localStorage.setItem('cart', JSON.stringify(cart))
      alert('Added to cart')
    }
  }
}
</script>
