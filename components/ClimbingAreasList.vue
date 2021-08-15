<template>
  <main class="bg-noise">
    <h1>Climbing Temps Beta</h1>
    <ClimbingArea v-for="climbingArea in climbingAreas"
                  :climbingArea="climbingArea"
    />
  </main>
</template>

<script>
import ClimbingArea from './ClimbingArea';
export default {
  name: 'ClimbingAreasList',
  components: {ClimbingArea},
  data() {
    return {
      climbingAreas: [
        {
          name: 'Mont-Wright',
          url: 'https://www.mountainproject.com/area/110151418/mont-wright',
          temps: [
            {
              timestamp: '1628996146',
              icon: '02d',
              description: 'few clouds',
              temp: '26',
              humidity: '69',
            },
            {
              timestamp: '1629082546',
              icon: '03d',
              description: 'clouds',
              temp: '21',
              humidity: '55',
            },
            {
              timestamp: '1629168946',
              icon: '01d',
              description: 'sunny',
              temp: '29',
              humidity: '5',
            },
          ]
        },
        {
          name: 'Val-Belair',
          url: 'https://www.mountainproject.com/area/108550529/val-belair',
          temps: [
            {
              timestamp: '1628996146',
              icon: '02d',
              description: 'few clouds',
              temp: '26',
              humidity: '69',
            },
            {
              timestamp: '1629082546',
              icon: '03d',
              description: 'clouds',
              temp: '21',
              humidity: '55',
            },
            {
              timestamp: '1629168946',
              icon: '01d',
              description: 'sunny',
              temp: '29',
              humidity: '5',
            },
          ]
        },
      ]
    }
  },
  mounted() {
    console.log(this.climbingAreas)
  }
};
</script>