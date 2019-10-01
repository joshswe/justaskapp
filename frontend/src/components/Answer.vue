<template>
    <div class="single-answer">
        <p class="text-muted">
            <strong>{{ answer.author }}</strong> &#8901; {{ answer.created_at }}
        </p>
        <p>{{ answer.body }}</p>

        <!-- Only the author of the answer can edit or delete his/her answer -->
        <div v-if="isAnswerAuthor">
            <!-- When the user clicks on the "Edit" button, he will be directed to the 'answer-editor' path -->
            <!-- The answer id will be passed in as the parameter -->
            <router-link 
                :to="{name : 'answer-editor', params: { id: answer.id }}"
                class="btn btn-sm btn-outline-secondary mr-1">Edit</router-link>
            
            <button class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">Delete</button>
        </div>

        <div v-else>
            <!-- Like button implementation
            Different visual effect if the user has already liked the answer -->
            <button class="btn btn-sm"
                @click="toggleLike"
                :class="{'btn-danger':userLikedAnswer,'btn-outline-danger': !userLikedAnswer}">
                <strong>Like [{{ likesCounter }}]</strong>
            </button>
        </div>
        <hr>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
    name: "AnswerComponent",
    data(){
        return {
            userLikedAnswer: this.answer.user_has_voted,
            likesCounter: this.answer.likes_count,
        }
    },
    props: {
        answer: {
            type: Object,
            required: true,
        },
        requestUser: {
            type: String,
            required: true,
        }
    },
    computed: {
        isAnswerAuthor(){
            return this.answer.author === this.requestUser
        }
    },
    methods: {
        triggerDeleteAnswer(){
            this.$emit("delete-answer",this.answer)
        },
        toggleLike(){
            this.userLikedAnswer === false ? this.likeAnswer():this.unlikeAnswer()
        },
        unlikeAnswer(){
            this.userLikedAnswer = false;
            this.likesCounter -= 1;
            let endpoint = `/api/answers/${ this.answer.id }/like/`;
            apiService(endpoint, "DELETE")
        },
        likeAnswer(){
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            let endpoint = `/api/answers/${ this.answer.id }/like/`;
            apiService(endpoint, "POST")
        }
    }
}
</script>