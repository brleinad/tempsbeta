<template>
  <section v-if="climbingArea" class="flex flex-row justify-between items-center rounded-2xl border-2 p-6 m-3 text-xs">
    <h3>{{ climbingArea.name }}</h3>
    <img :src="`http://openweathermap.org/img/wn/${climbingArea.temps[0].icon}.png`" alt=""/>
    <p>{{ climbingArea.temps[0].description }}</p>
    <p>{{ climbingArea.temps[0].temp }}&#176;</p>
    <p>{{ climbingArea.temps[0].humidity }}%</p>
  </section>
</template>

<script>

export default {
  name: 'ClimbingArea',
  props: {
   climbingArea: {
     type: Object,
     required: true,
   }
  },
  mounted() {
    console.log(this.climbingArea)
  }
};
</script>
