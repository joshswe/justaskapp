<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link :to="{ name: 'home' }" class="navbar-brand">JustAsk!</router-link>

            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <router-link :to="{ name: 'home' }" class="btn btn-sm btn-success">Home</router-link>
                </li>
                <li class="nav-item mx-2">
                    <router-link :to="{ name: 'question-editor' }" class="btn btn-sm btn-danger">Ask Question</router-link>
                </li>
                <li class="nav-item">
                    <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/">Welcome {{ currentUser }},Logout</a>
                </li>
            </ul>
        </div>
    </nav>
</template>


<script>
export default {
    name: "NavbarComponent",
    props: {
        currentUser: {
            type: String,
            required: true,
        }
    }
};
</script>

<style scoped>
.my-navbar {
    border-bottom: 1px solid #ddd;
}

.navbar-brand {
    font-weight: bold;
    font-size: 200%;
}

.navbar-brand:hover {
    color: #dc3545 !important;
}
</style>