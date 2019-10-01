import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Question from "./views/Question.vue"
import QuestionEditor from "./views/QuestionEditor.vue"
import AnswerEditor from "./views/AnswerEditor.vue"
import NotFound from "./views/NotFound.vue"
Vue.use(Router);

export default new Router({
  mode: "history",
  //base: process.env.BASE_URL,


  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/question/:slug",
      name: "question",
      component: Question,
      props: true
    },
    {
      path: "/addquestion/:slug?",
      name: "question-editor",
      component: QuestionEditor,
      props: true
    },
    {
      path: "/answer/:id",
      name: "answer-editor",
      component: AnswerEditor,
      props: true
    },
    {
      path: "*",
      name: 'page-not-found',
      component: NotFound,
    }

  ]
});
