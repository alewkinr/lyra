<template>
  <div class="flex items-center align-middle justify-center w-full h-full">
    <div
      class="min-w-64 w-1/4 p-4 bg-white border border-gray-200 shadow rounded"
    >
      <form @submit="loginReq">
        <p class="font-medium text-gray-700 text-lg text-center w-full">
          Вход в систему
        </p>
        <div class="mt-2">
          <label
            for="email"
            class="block text-sm font-medium leading-5 text-gray-700"
            >Email</label
          >
          <input
            id="email"
            class="w-full border border-maingray rounded h-8 p-2"
            v-model="form.login"
          />
        </div>
        <div class="mt-2">
          <label
            for="password"
            class="block text-sm font-medium leading-5 text-gray-700"
            >Пароль</label
          >
          <input
            id="password"
            type="password"
            class="w-full border border-maingray rounded h-8 p-2"
            v-model="form.password"
          />
        </div>
        <button
          class="mt-2 w-full border border-gray-200 bg-mainblue color rounded text-white h-8"
        >
          Войти
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { AUTH_REQUEST } from "../../store/actions";
export default {
  data() {
    return {
      form: {
        login: null,
        password: null,
      },
    };
  },
  computed: {
    authState() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    authRedirect() {
      this.$router.push("/models");
    },
    checkRedirect() {
      if (this.authState) {
        this.authRedirect();
      }
    },
    loginReq(e) {
      e.preventDefault();
      this.$store.dispatch(AUTH_REQUEST, this.form);
    },
  },
  mounted() {
    this.checkRedirect();
  },
};
</script>

<style>
</style>