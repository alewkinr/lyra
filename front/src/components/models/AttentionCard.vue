<template>
  <div
    :style="boxStyle"
    class="border border-l-4 rounded space-y-4 flex flex-col p-4 text-lg text-textblack bg-white"
  >
    <div class="grid grid-cols-2 gap-4">
      <div class="col-span-2"> 
        <span class=" font-medium ">Модель 1: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.2)</span>
        <span class="ml-2 text-red-500 font-medium">деградация</span>
      </div>
      <div class="col-span-2">
        <span class=" font-medium">Изменение статуса: </span>
        <span class="ml-1">13.11.2020 4:20</span>
      </div>
      <div>
        <span class=" font-medium">Точность: </span>
        <span class="ml-1">78%</span>
      </div>
      <div>
        <span class="font-medium">Статистика Колмогорова-Смирнова: </span>
        <span class="ml-1">0.312</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["variant"],
  data() {
    return {
      // sidecolor: ''
    };
  },
  computed: {
    boxStyle() {
      return {
        "border-left": `4px solid ${this.variant ? this.variant : "#f56565"}`,
      };
    },
  },
};
</script>

<style>
</style>