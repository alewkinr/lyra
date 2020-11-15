<template>
  <div
    :style="boxStyle"
    class="border rounded space-y-4 flex flex-col p-4 text-lg text-textblack"
  >
    <div class="grid grid-cols-2 gap-4">
        <div class="mb-4 col-span-2">
        <span class="font-medium">Проект: </span>
        <span class="ml-1">Отдел цифровых разработок</span>
        <span class="ml-2 text-gray-500">(3 модели)</span>
      </div>
      <div class="col-span-2" @click="$router.push('/models/1')"> 
        <span class=" font-medium ">Модель 1: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.2)</span>
        <span class="ml-2 text-green-500 font-medium">стабильна</span>
      </div>
      <div class="col-span-2" @click="$router.push('/models/1')"> 
        <span class=" font-medium ">Модель 2: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.2)</span>
        <span class="ml-2 text-red-500 font-medium">деградация</span>
      </div>
      <div class="col-span-2" @click="$router.push('/models/1')"> 
        <span class="font-medium ">Модель 3: </span>
        <span class="ml-1 text-mainblue underline cursor-pointer">nm18.py</span>
        <span class="ml-2 text-gray-500">(версия 0.2)</span>
        <span class="ml-2 text-green-500 font-medium">стабильна</span>
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
        // "border-left": `4px solid ${this.variant ? this.variant : "#374FFF"}`,
      };
    },
  },
};
</script>

<style>
</style>