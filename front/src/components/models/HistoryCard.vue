<template>
  <div
    :style="boxStyle"
    class="border border-l-4 rounded space-y-4 flex flex-col p-4 text-lg text-textblack"
  >
    <div class="grid grid-cols-2 gap-4">
      <div class="col-span-2">
        <span class="font-medium">Событие: </span>
        <span class="ml-1 cursor-pointer">Обучение завершено</span>
      </div>
      <div>
        <span class="font-medium">Версия: </span>
        <span class="ml-1 cursor-pointer">0.1</span>
      </div>
      <div>
        <span class="font-medium">Размер выборки: </span>
        <span class="ml-1 cursor-pointer">7224</span>
      </div>
      <div>
        <span class="font-medium">Дата изменения: </span>
        <span class="ml-1 cursor-pointer">15.11.2020 12:00</span>
      </div>
      <div>
        <span class="font-medium">Дата обучения: </span>
        <span class="ml-1 cursor-pointer">15.11.2020 12:00</span>
      </div>
      <div>
        <span class="font-medium">Метрика качества: </span>
        <span class="ml-1 cursor-pointer">97%</span>
      </div>
      <div>
        <span class="font-medium">Время обучения: </span>
        <span class="ml-1 cursor-pointer">10 минут</span>
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