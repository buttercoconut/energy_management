<template>
  <div id="app">
    <nav>
      <router-link to="/">Dashboard</router-link> |
      <router-link to="/report">Report</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
// No script needed
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}
nav {
  background: #42b983;
  padding: 1rem;
  color: white;
}
nav a {
  color: white;
  text-decoration: none;
  margin: 0 0.5rem;
}
</style>
