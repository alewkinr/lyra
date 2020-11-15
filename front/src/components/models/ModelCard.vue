<template>
  <div class="h-full flex w-full">
    <div class="h-full w-8/12 bg-white pl-5 pr-5 space-y-6 text-textblack">
      <div class="pt-5 w-full flex align-middle items-center">
        <div class="p-1 cursor-pointer" @click="$router.push('/models')">
          <unicon name="ui-arrow-back" fill="#374FFF" viewBox="0 0 21 8" />
        </div>
        <div class="pl-4 text-textblack font-semibold leading-4 text-xl">
          Модель n18
        </div>
        <div class="pl-4 text-green-500 font-medium">стабильна</div>
        <div class="flex-grow"></div>
        <div class="text-blue-500 font-normal text-md">
          Версия:
          <select class="w-16">
            <option>0.1</option>
            <option selected>0.2</option>
          </select>
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

      <!-- Информация -->
      <div class="" v-if="activeTab === 'info'">
        <div class="border rounded space-y-4 flex flex-col p-4 text-lg">
          <div>
            <span class="font-medium">Описание: </span>Наиболее часто в
            современных экономических расчётах в качестве изучаемого признака
            берётся уровень годового дохода. Коэффициент Джини можно определить
            как макроэкономический показатель, характеризующий дифференциацию
            денежных доходов населения в виде степени отклонения фактического
            распределения доходов от абсолютно равного их распределения между
            жителями страны.
          </div>
          <div>
            <span class="font-medium">Последнее обновление: </span>16.11.2020
          </div>
          <div><span class="font-medium">Стадия: </span>обучение завершено</div>
          <div>
            <span class="font-medium">Данные: </span
            ><span class="text-mainblue underline cursor-pointer"
              >transactions.csv</span
            >
          </div>
        </div>
      </div>

      <!-- Тесты -->
      <div class="space-y-6" v-if="activeTab === 'tests'">
        <TestCard v-for="j in 3" :key="j"></TestCard>
      </div>

      <!-- Переобучение -->
      <div class="" v-if="activeTab === 'retrain'">
        <div class="border rounded space-y-6 flex flex-col p-4 text-lg">
          <div class="flex items-center">
            <div
              class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow"
            >
              <unicon
                name="ui-cloud-upload"
                fill="#374FFF"
                viewBox="0 0 20 20"
              />
            </div>
            <span class="ml-4 font-medium">Модель: </span>
            <span class="ml-2 text-mainblue underline cursor-pointer"
              >nm18.py</span
            >
            <span class="ml-2 text-gray-500">(версия 0.2)</span>
          </div>
          <div class="flex items-center">
            <div
              class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow"
            >
              <unicon
                name="ui-cloud-upload"
                fill="#374FFF"
                viewBox="0 0 20 20"
              />
            </div>
            <span class="ml-4 font-medium">Данные: </span>
            <span class="ml-2 text-mainblue underline cursor-pointer"
              >transactions.csv</span
            >
            <span class="ml-2 text-gray-500">(текущий датасет)</span>
          </div>
          <div
            class="border rounded-md h-16 box-border w-full p-4 flex flex-col"
          >
            <div
              class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
            >
              Прогнозируемое значение
            </div>
            <input class="w-full text-textblack" value="Экономика" />
          </div>
          <div class="flex items-center">
            <div
              class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow cursor-pointer"
              @click="related.push({ type: 'String', name: '' })"
            >
              <unicon name="ui-plus-blank" fill="#374FFF" viewBox="0 0 16 16" />
            </div>
            <span class="ml-4 font-medium"
              >От каких колонок зависит прогнозируемое значение?</span
            >
          </div>
          <div
            class="border rounded-md h-16 box-border w-full p-4 flex flex-col"
            v-for="(item, index) in related"
            :key="index"
          >
            <div
              class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
            >
              {{ item.type }}
            </div>
            <div class="w-full flex items-center">
                <input class="flex-grow text-textblack" :value="item.name" />
                <unicon name="times" @click="related.splice(index, 1)"></unicon>
            </div>
          </div>
          <div class="flex items-center">
            <div
              class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow cursor-pointer"
              
            >
              <unicon name="ui-plus-blank" fill="#374FFF" viewBox="0 0 16 16" />
            </div>
            <span class="ml-4 font-medium"
              >Добавить дополнительные колонки расширенными средствами?</span
            >
          </div>
          <div class="flex items-center">
            <div
              class="w-12 h-12 p-2 border flex justify-center items-center rounded-md shadow cursor-pointer"
              
            >
              <unicon name="ui-plus-blank" fill="#374FFF" viewBox="0 0 16 16" />
            </div>
            <span class="ml-4 font-medium"
              >Какие записи должны попасть в обучающую выборку?</span
            >
          </div>

          <div
            class="border rounded-md h-16 box-border w-full p-4 flex flex-col"
          >
            <div
              class="text-sm text-gray-500 -mt-8 -ml-2 h-8 bg-white pl-2 pr-2 w-fit"
            >
              Колонка для сохранения результата
            </div>
            <input class="w-full text-textblack" value="Экономика" />
          </div>
        </div>
      </div>
      <!-- 
          
          
          История 
          
          
          -->
      <div v-if="activeTab === 'history'" class="space-y-6">
        <HistoryCard v-for="j in 3" :key="j"></HistoryCard>
      </div>
    </div>
    <div
      class="w-full h-full pl-10 pr-10 flex flex-col space-y-5 overflow-scroll"
    >
      <div
        class="pt-5 pl-10 w-full text-textblack font-semibold leading-6 text-xl"
      >
        Метрики
      </div>
      <ChartCard v-for="i in 3" :key="i" title="Коэффициент Джини"></ChartCard>
    </div>
  </div>
</template>

<script>
import ChartCard from "./ChartCard";
import HistoryCard from './HistoryCard'
import TestCard from "./TestCard"
export default {
  components: {
    ChartCard,
    TestCard,
    HistoryCard
  },
  data() {
    return {
      activeTab: "info",
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
          key: "info",
          name: "Информация",
        },
        {
          key: "tests",
          name: "Тестирование",
        },
        {
          key: "retrain",
          name: "Переобучение",
        },
        {
          key: "history",
          name: "История",
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
</style>