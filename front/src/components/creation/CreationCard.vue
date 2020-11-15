<template>
  <div class="h-full flex w-full">
    <div class="h-full w-8/12 bg-white pl-5 pr-5 space-y-6 text-textblack overflow-scroll">
      <div class="pt-5 w-full flex align-middle items-center">
        <div class="pl-4 text-textblack font-semibold leading-4 text-xl">
          Модели и данные
        </div>
      </div>

      <!-- Таб селектор -->
      <div class="w-full mt-16">
        <div class="inline-flex w-full">
          <button
            class="tab-selector border border-r-0 hover:bg-gray-400 text-gray-800 font-medium py-2 px-4 flex-grow"
            v-for="(tab, index) in tabs"
            :key="tab.key"
            :class="getTabClass(tab, index)"
            @click="activeTab = tab.key"
          >
            {{ tab.name }}
          </button>
        </div>
      </div>
      <!-- 
          История 
          -->
      <div v-if="activeTab === 'models'" class="space-y-6">
        <div class="border rounded-md h-16 box-border w-full p-4 flex flex-col">
          <div
            class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
          >
            Название
          </div>
          <input class="w-full text-textblack" value="Модель" />
        </div>

        <div class="border rounded-md h-16 box-border w-full p-4 flex flex-col">
          <div
            class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
          >
            Описание
          </div>
          <input class="w-full text-textblack" value="Модель" />
        </div>

        <div class="flex items-center">
          <div
            class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow cursor-pointer"
          >
            <unicon name="ui-cloud-upload" fill="#374FFF" viewBox="0 0 20 20" />
          </div>
          <span class="ml-4 font-medium">Модель: </span>
          <span class="ml-2 text-mainblue underline cursor-pointer"
            >file.py</span
          >
        </div>
        <div class="flex items-center">
          <div
            class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow cursor-pointer"
          >
            <unicon name="ui-cloud-upload" fill="#374FFF" viewBox="0 0 20 20" />
          </div>
          <span class="ml-4 font-medium">Данные: </span>
          <span class="ml-2 text-mainblue underline cursor-pointer"
            >transactions.csv</span
          >
        </div>

        <div class="flex items-center">
          <div
            class="flex justify-center items-center cursor-pointer"
            @click="autocheck = !autocheck"
          >
            <div class="relative">
              <!-- input -->
              <input v-model="autocheck" type="checkbox" class="hidden" />
              <!-- line -->
              <div
                class="toggle__line w-12 h-6 bg-gray-400 rounded-full shadow-inner"
              ></div>
              <!-- dot -->
              <div
                class="toggle__dot absolute w-6 h-6 bg-white rounded-full shadow inset-y-0 left-0"
              ></div>
            </div>
          </div>
          <span class="ml-4 font-medium">Автоматиечески обновлять модель?</span>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div
            class="border rounded-md h-16 box-border w-full p-4 flex flex-col"
          >
            <div
              class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
            >
              Переобучать через
            </div>
            <input class="w-full text-textblack" value="30" />
          </div>
          <div
            class="border rounded-md h-16 box-border w-full p-4 flex flex-col"
          >
            <div
              class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
            >
              Нижний порог точности
            </div>
            <input class="w-full text-textblack" type="numeric" value="80" />
          </div>
        </div>

        <div class="flex items-end w-full flex-row-reverse">
          <button
            class="shadow border rounded-lg p-3 text-mainblue font-semibold"
            @click="
              $router.push('/models')
            "
          >
            Создать
          </button>
        </div>
      </div>
    </div>
    <div
      class="w-full h-full pl-10 pr-10 flex flex-col space-y-5 overflow-scroll"
    ></div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      activeTab: "models",
      autocheck: true,
      chartStyles: {
        height: "300px",
        width: "100%",
      },
      related: [
        {
          type: "Number",
          name: "Возраст",
        },
        {
          type: "String",
          name: "Пол",
        },
      ],
      tabs: [
        {
          key: "models",
          name: "Модели",
        },
        {
          key: "data",
          name: "Данные",
        },
        {
          key: "metrics",
          name: "Метрики",
        },
      ],
    };
  },
  methods: {
    getTabClass(tab, index) {
      let classes = "";
      if (index === 0) {
        classes += "rounded-l-lg ";
      }
      if (index === this.tabs.length - 1) {
        classes += "rounded-r-lg ";
      }
      if (tab.key === this.activeTab) {
        classes += "active ";
      }
      return classes;
    },
  },
};
</script>

<style>
.tab-selector.active {
  @apply bg-mainblue;
  @apply text-white;
}

.toggle__dot {
  top: -0.25rem;
  left: -0.25rem;
  transition: all 0.3s ease-in-out;
}

input:checked ~ .toggle__dot {
  transform: translateX(100%);
}

input:checked ~ .toggle__line {
  @apply bg-green-600;
}
</style>