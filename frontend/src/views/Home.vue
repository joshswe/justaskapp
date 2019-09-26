<template>
    <div class="home">
        <div class="container">
            <div v-for="question in questions" :key="question.pk">
                <p class="mb-0">
                    Posted by:
                    <span>{{ question.author }}</span>
                </p>
                <h2>{{ question.content }}</h2>
                <p>Answers: {{ question.answers_count }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import  { getJSON} from "../common/api.service";
export default {
    name: "home",
    data() {
        return {
            questions: []
        };
    },
    methods: {
        getQuestions() {
            // API endpoints were set in Django REST
            let endpoint = "/api/questions/";
            console.log("getQuestions function is called!");
            // console.log("apiService(endpoint) returns:", apiService(endpoint))
            // apiService(endpoint).then(response => { 
            //   console.log(response.clone().json())
            //   return response.clone().json();
            // }).then(data => {
            //   console.log(data)
            //   this.questions.push(... data)
            // })

            apiService(endpoint).then(data => {this.questions.push(... data)})

        }
    },

    // Call the APIs once the webpage is requested
    // See Instance Lifecycle Hooks: https://vuejs.org/v2/guide/instance.html
    created: function() {
        console.log("Instance Lifecycle Hooks begins!");
        this.getQuestions();
        console.log("Questions:", this.questions);
    }
};
</script>
