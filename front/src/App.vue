<template>
  <div id="app">
    <div class="menu w-100px h-screen border border-gray-200 flex flex-col">
      <div class="flex flex-col" style="padding: 24px;">
        <img src="./assets/logo.svg" >
        <!-- <MenuButton icon="setting"></MenuButton> -->
      </div>
      <div class="flex-grow justify-center align-middle flex flex-col">
        <MenuButton icon="ui-box" route="/models"></MenuButton>
        <MenuButton icon="ui-chart" route="/comparison"></MenuButton>
        <MenuButton icon="ui-gear" ></MenuButton>
      </div>
      <div class="flex flex-col">
        <MenuButton icon="ui-plus" route="/creation"></MenuButton>
      </div>
    </div>
    <div class="bg-bgblue w-full h-full">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import MenuButton from "./components/ui/MenuButton";
export default {
  name: "App",
  components: { MenuButton },
  computed: {},
};
</script>

<style>
#app {
  width: 100%;
  height: 100vh;
  display: flex;
  font-family: 'Gilroy';
}
</style>
