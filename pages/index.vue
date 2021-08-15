<template>
  <div class="bg-noise h-screen">
    <ClimbingAreasList />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ClimbingAreasList from "~/components/ClimbingAreasList.vue";

export default Vue.extend({
  components: {ClimbingAreasList}
})
</script>
