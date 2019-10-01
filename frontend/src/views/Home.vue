<template>
    <div class="home">
        <div class="container">
            <br>
            <!-- Display a list of question in Home Page -->
            <div v-for="question in questions" :key="question.pk">
                <p class="mb-0">
                    Posted by:
                    <span class="question-author">{{ question.author }}</span>
                </p>
                <h2>
                    <router-link :to="{ name: 'question', params : { slug: question.slug } }" class="question-link">
                        {{ question.content }}
                    </router-link>
                </h2>
                <p>Answers: {{ question.answers_count }}</p>
                <hr>
            </div>
            <!-- Load more questions button will be implemented later
            <div class="my-4">
                <p v-show="loadingQuestions">...loading...</p>
                <button v-show="next" @click="getQuestions" class="btn btn-sm btn-outline-success">
                    Load More
                </button>
            
            </div> -->
        </div>
    </div>
</template>

<script>
// Import functions/components
import { apiService } from "../common/api.service";
import  { getJSON} from "../common/api.service";

// Create local registration for Vue component
export default {
    name: "home",
    data() {
        return {
            questions: [],
            next: null,
            loadingQuestions: false,
        };
    },
    methods: {
        getQuestions() {
            // API endpoints were set in Django REST
            let endpoint = "/api/questions/";
            if (this.next){
                endpoint = this.next;
            }
            this.loadingQuestions = true;

            // //Test the promise
            // console.log("apiService(endpoint) returns:", apiService(endpoint))
            // apiService(endpoint).then(response => { 
            //   console.log(response.clone().json())
            //   return response.clone().json();
            // }).then(data => {
            //   console.log(data)
            //   this.questions.push(... data)
            // })

            apiService(endpoint)
                .then(data => {
                    this.questions.push(... data)
                    this.loadingQuestions = false;
                    if (data.next){
                        this.next = data.next;
                    }else{
                        this.next = null;
                    }
                    
                })

        }
    },

    // Call the APIs once the webpage is requested
    // See Instance Lifecycle Hooks: https://vuejs.org/v2/guide/instance.html
    created: function() {
        console.log("Instance Lifecycle Hooks begins!");
        this.getQuestions();
        console.log("Questions:", this.questions);
        document.title = "Home - JustAsk!"
    }
};
</script>

<style scoped>

.question-author {
    font-weight: bold;
    color: #dc3545;
}

.question-link {
    font-weight: bold;
    color: black;
}

.question-link:hover {
    color: #343a40;
    text-decoration: none;
}
</style>