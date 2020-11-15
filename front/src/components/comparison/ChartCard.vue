<template>
  <div
    class="w-full p-5 bg-white rounded border border-maingray space-y-4 shadow h-400px"
  >
    <div class="pl-5 text-textblack text-lg font-semibold">
      {{ title }}
    </div>
    <bar-chart
      :chart-data="datacollection"
      :styles="chartStyles"
      :options="options"
    ></bar-chart>
  </div>
</template>

<script>
import BarChart from "../ui/BarChart";
export default {
  props: ["title", "data"],
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
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  components: {
    BarChart,
  },

  mounted() {
    this.fillData();
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
        labels: [this.title],
        datasets: [
          {
            label: "Модель 1",
            backgroundColor: "#A8DCFF",
            data: [this.getRandomInt()],
          },
          {
            label: "Модель 2",
            backgroundColor: "#A8DCFF",
            data: [this.getRandomInt()],
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