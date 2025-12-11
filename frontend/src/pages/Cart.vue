<template>
  <div class="p-4">
    <h2>Your Cart</h2>
    <div v-if="items.length===0">Cart is empty</div>
    <div v-else>
      <div v-for="(it,idx) in items" :key="idx" style="border:1px solid #ccc; padding:8px; margin:8px 0;">
        <h3>{{ it.product.title }} — ₹{{ it.product.price }}</h3>
        <p>Quantity: {{ it.quantity }}</p>
      </div>
      <button @click="checkout">Checkout (demo)</button>
    </div>
  </div>
</template>

<script>
export default {
  data(){ return { items: [] } },
  mounted(){
    this.items = JSON.parse(localStorage.getItem('cart')||'[]')
  },
  methods:{
    checkout(){
      alert('Demo checkout — implement API call to create Order')
      localStorage.removeItem('cart')
      this.items = []
    }
  }
}
</script>
