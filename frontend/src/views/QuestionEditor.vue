<template>
    <div class="container mt-2">
        <h1 class="mb-3">Ask a Question</h1>
        <form @submit.prevent="onSubmit">
            <textarea v-model="question_body" 
                    rows="3" 
                    class="form-control" 
                    placeholder="Edit Your Question Here"></textarea>
            <br>
            <button type="submit" class="btn btn-success">Publish</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
    name: "QuestionEditor",
    data() {
        return {
            question_body: null,
            error: null
        }
    },
    methods:{
        // Validate the user's input
        onSubmit(){
            if (!this.question_body){
                this.error = "You can't send an empty question!";
            } else if (this.question_body.length > 240){
                this.error = "The maximum number of characters you can enter is 240";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";
                apiService(endpoint,method, {content: this.question_body })
                    .then(question_data => {

                        // Navigate to a different URL
                        this.$router.push({ name: 'question', 
                                            params : { slug: question_data.slug } })
                    })
            }
        }
    },
    created() {
        document.totle =" Edit Your Question";
    }
}
</script>