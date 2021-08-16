<template>
  <section v-if="climbingArea" class="flex flex-row justify-between items-center rounded-2xl border-2 p-6 m-3 text-xs">
    <h3 class="w-1/5">{{ climbingArea.name }}</h3>
    <div class="w-4/5 flex flex-row">
      <div v-for="temp in climbingArea.temps" class="flex flex-col">
        <img :src="`http://openweathermap.org/img/wn/${temp.icon}.png`" alt=""/>
        <p>{{ temp.description }}</p>
        <p>{{ temp.temp }}&#176;</p>
        <p>{{ temp.humidity }}%</p>
      </div>
    </div>
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
