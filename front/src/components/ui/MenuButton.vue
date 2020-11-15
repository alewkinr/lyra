<template>
  <div
    class="menu-button flex align-middle justify-center cursor-pointer select-none"
    @mouseover="type = true"
    @mouseleave="type = false"
  >
    <unicon :name="icon" :icon-style="styleIcon" :fill="fill" :viewBox="vbox" @click="$router.push(route)"/>
  </div>
</template>

<script>
export default {
  props: ["icon", "forcestyle", "route"],
  data() {
    return {
      type: false,
      customVboxes: {
        'ui-box': 30,
        'ui-chart': 26,
        'ui-gear': 26,
        'ui-plus': 36
      }
    };
  },
  computed: {
    styleIcon() {
      if (this.forcestyle) {
        return this.forcestyle
      }
      return this.type ? "monochrome" : "line";
    },
    vbox() {
      if (this.icon in this.customVboxes) {
        return `0 0 ${this.customVboxes[this.icon]} ${this.customVboxes[this.icon]}`
      }
      return `0 0 24 24`
    },
    fill() {
      if (this.icon in this.customVboxes && !this.type) {
        return 'white'
      }
      return "#374FFF"
    }
  },
};
</script>

<style lang="scss">
.menu-button {
  padding: 25px;
  svg {
    width: 30px;
    height: 30px;
  }
}
</style>