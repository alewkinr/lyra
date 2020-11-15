<template>
  <div
    :style="boxStyle"
    class="border border-l-4 rounded space-y-4 flex flex-col p-4 text-lg text-textblack"
  >
    <div class="grid grid-cols-2 gap-4">
      <div>
        <span class="font-medium">Модель 1: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.2)</span>
      </div>
      <div>
        <span class="font-medium">Модель 2: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.1)</span>
      </div>
      <div>
        <span class="font-medium">Данные: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer"
          >transaction.csv</span
        >
      </div>
      <div></div>
      <div>
        <span class="font-medium">Начала теста: </span>
        <span class="ml-1 cursor-pointer">15.11.2020 10:00</span>
      </div>
      <div>
        <span class="font-medium">Окончание теста: </span>
        <span class="ml-1 cursor-pointer">15.11.2020 12:00</span>
      </div>
      <div>
        <span class="font-medium">Точность: </span>
        <span class="ml-1 cursor-pointer">97% / 60%</span>
      </div>
      <div>
        <span class="font-medium">Стабильность: </span>
        <span class="ml-1 cursor-pointer">80% / 65%</span>
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
        "border-left": `4px solid ${this.variant ? this.variant : "#374FFF"}`,
      };
    },
  },
};
</script>

<style>
</style>