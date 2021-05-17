import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Question from "../views/Question.vue";
import QuestionEditor from "../views/QuestionEditor.vue";
import AnswerEditor from "../views/AnswerEditor.vue";
import NotFound from "../views/NotFound.vue";



Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/question/:slug",
    name: "question",
    component: Question,
    props: true
  },
  {
    //? means that mabye will be passed, and if passed then use it as a prop
    path: "/ask/:slug?",
    name: "question-editor",
    component: QuestionEditor,
    props: true
  },
    {
    path: "/answer/:id",
    name: "answer-editor",
    component: AnswerEditor,
    //the passed :id will be used as a prop in the AnswerEditor
    props: true
  },
    {
    path: "*",
    name: "page-not-found",
    component: NotFound,
    //the passed :id will be used as a prop in the AnswerEditor
    props: true
  },

];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes,
});

export default router;
