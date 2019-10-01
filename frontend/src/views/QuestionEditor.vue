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
    props: {
        slug: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            question_body: null,
            error: null
        }
    },
    methods:{
        
        onSubmit(){
            if (!this.question_body){
                this.error = "You can't send an empty question!";
            } else if (this.question_body.length > 240){
                this.error = "The maximum number of characters you can enter is 240";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";

                // User is editing the question if there is a slug
                if (this.slug !== undefined){
                    endpoint += `${ this.slug }/`;
                    method = "PUT";
                }
                apiService(endpoint,method, {content: this.question_body })
                    .then(question_data => {

                        // Navigate to the new question URL: /question/<quesiton slug>
                        this.$router.push({ name: 'question', 
                                            params : { slug: question_data.slug } })
                    })
            }
        }
    },
    async beforeRouteEnter(to,from,next){
        // Check does the question exist by validating the slug
        if (to.params.slug !== undefined){
            // GET request is made to get the content of the question that the user tries to edit
            let endpoint = `/api/questions/${ to.params.slug }/`;
            let data = await apiService(endpoint);
            return next(vm => (vm.question_body = data.content))
        } else {
            return next()
        }
    },
    created() {
        document.title = "Add or Edit Your Question";
    }
}
</script>