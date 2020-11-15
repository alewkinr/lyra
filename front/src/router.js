import VueRouter from "vue-router";
import Vue from "vue";
import LoginPage from "./components/auth/LoginPage";
import models from './routes/models'
import creation from './routes/creation'
import comparison from './routes/comparison'
Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes: [
    { path: "/", redirect: "/login" },
    {
      path: "/login",
      component: LoginPage,
      name: "Login",
      meta: { isPublic: true },
    },
    ...models,
    ...creation,
    ...comparison
  ],
});
export default router;
