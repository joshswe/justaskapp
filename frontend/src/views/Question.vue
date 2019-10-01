<template>
    <div class="single-question mt-2">
        <div v-if="question" class="container">
            <h1>{{ question.content }}</h1>
            <QuestionActions
                v-if="isQuestionAuthor"
                :slug="question.slug"/>
            <br>
            <p class="mb-0">
                Posted by:
                <span class="author-name">{{ question.author }}</span>
            </p>
            <p> {{ question.created_at }}</p>
            <hr>

            <!-- If the user has already answered the question, a message "You have already submitted an answer!" will show up -->
            <div v-if="userHasAnswered">
                <p class="answer-added">You have already submitted an answer!</p>
            </div>

            <!-- If the user has already answered the question and clicked on the "Answer the Question" button, there will be a text box area -->
            <div v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Answer the Question
                    </div>
                    <div class="card-block">
                        <textarea v-model="newAnswerBody" class="form-control" placeholder="Type your answer here..." rows=5></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sn btn-success">Submit Your Answer</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">{{ error }}</p>
            </div>

            <!-- Else the user will see the "Answer the Question" button-->
            <div v-else>
                <button class="btn btn-sm btn-success" @click="showForm=true">
                    Answer the Question
                </button>

            </div>

            <hr>
        </div>
        <div v-else>
            <h1 id="notfound">404 - Question Not Found</h1>
        </div>
        <div v-if="question" class="container">
            <AnswerComponent
                v-for="(answer,index) in answers"
                :answer="answer"
                :requestUser="requestUser"
                :key="index"
                @delete-answer="deleteAnswer"
            />
        </div>
    </div>
</template>

<script>
// Import functions/components
import { apiService } from "../common/api.service";
import AnswerComponent from "../components/Answer.vue";
import QuestionActions from "../components/QuestionActions.vue";

// Create local registration for Vue component
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components:{
        AnswerComponent,
        QuestionActions
    },
    data() {
        return {
            question: {},
            answers: [],
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false,
            requestUser: null,
        }
    },
    computed: {
        isQuestionAuthor(){
            return this.question.author === this.requestUser
        }
    },
    methods: {
        
        // Get Question Data
        getQuestionData(){
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint).then(data => {
                if (data){
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered;
                    this.setPageTitle(data.content)
                }else {
                    this.question = null;
                    this.setPageTitle("404 - Page Not Found")
                }
            })
        },

        // Set the Title of the Page to Question Title
        setPageTitle(title){
            document.title = title;
        },
        getQuestionsAnswers(){
            let endpoint = `/api/questions/${this.slug}/answers/`;
            apiService(endpoint)
                .then(data => {
                    this.answers = data;
                })
        },

        // Run this function when the Submit button is clicked
        onSubmit(){
            if(this.newAnswerBody){
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", {body:this.newAnswerBody})
                    .then(data => {
                        // Add the new answer to the beginning of the "answers" array
                        this.answers.unshift(data)
                    })
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if(this.error){
                    this.error = null;
                }
            } else{
                this.error = "You can't send an empty answer!";
            }
        },
        setRequestUser(){
            this.requestUser = window.localStorage.getItem("username");
        },
        async deleteAnswer(answer){
            let endpoint = `/api/answers/${answer.id}/`;
            try {
                await apiService(endpoint, "DELETE")
                this.$delete(this.answers,this.answers.indexOf(answer))
                this.userHasAnswered = false;

            }
            catch (err){
                console.log(err)
            }
        }
    },
    created: function() {
        this.getQuestionData();
        this.getQuestionsAnswers();
        this.setRequestUser();
        }
    }
</script>

<style scoped>
    .author-name {
        font-weight: bold;
        color: #dc3545;
    }

    .answer-added {
        font-weight: bold;
        color: green;
    }

    .error {
        font-weight:bold;
        color: red;
    }

    #notfound {
        color: red;
        text-align: center;
    }

</style>