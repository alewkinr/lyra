<template>
  <div
    class="w-full p-5 bg-white rounded border border-maingray space-y-4 shadow h-400px"
  >
    <div class="pl-5 text-textblack text-lg font-semibold">
      {{ title }}
    </div>
    <line-chart
      :chart-data="datacollection"
      :styles="chartStyles"
      :options="options"
    ></line-chart>
    <div class="flex justify-center items-center w-full">
      <div class="border rounded-3xl">
        <button
          class="period-selector rounded-3xl hover:bg-gray-400 text-gray-800 font-medium py-2 px-4"
          v-for="(tab, index) in periods"
          :key="tab.key"
          :class="getTabClass(tab, index)"
          @click="activeTab = tab.key"
        >
          {{ tab.name }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "../ui/LineChart";
export default {
  props: ["title", "content"],
  data() {
    return {
      activeTab: "month",
      periods: [
        {
          key: "year",
          name: "Год",
        },
        {
          key: "month",
          name: "Месяц",
        },
        {
          key: "week",
          name: "Неделя",
        },
        {
          key: "day",
          name: "День",
        },
      ],
      chartStyles: {
        position: "relative",
        height: "300px",
      },
      datacollection: {},
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  components: {
    LineChart,
  },
  mounted() {
    if (!this.content) {
      this.fillData();
    } else {
      this.datacollection = {
        labels: this.content.cols,
        datasets: [
          {
            label: this.title,
            backgroundColor: "#A8DCFF",
            data: this.content.vals,
          },
        ],
      };
    }
  },
  methods: {
    getTabClass(tab, index) {
      let classes = "";
      if (index === 0) {
        classes += " ";
      }
      // if (index === this.periods.length - 1) {
      //   classes += "border-r";
      // }
      if (tab.key === this.activeTab) {
        classes += "active ";
      }
      return classes;
    },
    fillData() {
      this.datacollection = {
        labels: [
          this.getRandomInt(),
          this.getRandomInt(),
          this.getRandomInt(),
          this.getRandomInt(),
          this.getRandomInt(),
        ],
        datasets: [
          {
            label: this.title,
            backgroundColor: "#A8DCFF",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
            ],
          },
        ],
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
  },
};
</script>

<style>
.period-selector.active {
  @apply border-mainblue;
  @apply border;
}
</style>