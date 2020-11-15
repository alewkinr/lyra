<template>
  <div class="h-full flex w-full">
    <div class="h-full w-8/12 bg-white pl-5 pr-5 space-y-6 text-textblack">
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
        <ProjectCard v-for="i in 1" :key="i"></ProjectCard>
      </div>
    </div>
    <div
      class="w-full h-full pl-10 pr-10 flex flex-col space-y-5 overflow-scroll"
    >
      <div
        class="pt-5 pl-10 w-full text-textblack font-semibold leading-6 text-xl"
      >
        Требуют внимания
      </div>
      <AttentionCard v-for="i in 3" :key="i"></AttentionCard>
    </div>
  </div>
</template>

<script>
import AttentionCard from "./AttentionCard";
import ProjectCard from "./ProjectCard";
export default {
  components: {
    AttentionCard,
    ProjectCard
  },
  data() {
    return {
      activeTab: "models",
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
        }
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