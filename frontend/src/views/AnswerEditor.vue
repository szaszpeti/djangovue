<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Answer</h1>
    <form @submit.prevent="onSubmit">
      <textarea 
        v-model="answerBody" 
        class="form-control" 
        rows="3"
      ></textarea>
      <br>
      <button 
        type="submit" 
        class="btn btn-success"
        >Publish your answer
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      questionSlug: null,
      answerBody: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody })
          .then(() => {
            this.$router.push({
              name: "question",
              params: { slug: this.questionSlug }
            })
          })
      } else {
        this.error = "You can't submit an empty answer!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(vm => (
      vm.answerBody = data.body,
      vm.questionSlug = data.question_slug
    ));
  }
};
</script>




<!-- 
  mathods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`
        apiService(endpoint, "PUT", {body: this.answerBody})
          //use it to redirect the user to the question where this answer was added
          .then(() => {
            this.$router.push({
              name: "question",
              params: {slug: this.questionSlug}
            })
          })


      } else {
        this.error = "You can not add an empty answer!"
      }
    }
  },
  //to=target root object navigated to, from=current root navigated away from, //next=function we //use to move 
  //before entering the root itself this one will be called
  //it will use the :id parameter send by Answer.vue
  //so it returns the data we trying to edit
  async beforeRoutEnter(to, from, next) {

    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
   
    //to.params.previousAnswer = data.body;
    //to.params.questionSlug = data.question_slug;
    //vm refers to the component itself here 
    return next(vm => (
      vm.answerBody = data.body,
      vm.questionSlug = data.question_slug
      ));

  }
}
</script> -->