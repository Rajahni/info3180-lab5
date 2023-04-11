<script setup>
    import { ref, onMounted } from "vue";


    let movies = ref([]);
    let loading = ref(false);

    onMounted(() => {
        loading.value = true;

        fetch("api/v1/movies", {
            method: "GET",
        })
        .then((resp) => resp.json())
        .then((data) => {
            movies.value = data.movies;
            loading.value = false;
        })
        .catch((err) => {
            console.log(err)
            loading.value = false;
            // error.value = "Unable to fetch your articles";
        })
    });
</script>

<template>
    <main class="container py-5">
        <h1 class="display-1 mb-3">Movies</h1>
        <div v-if="loading" class="d-flex justify-content-center">
            <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <ul v-if="!loading">
            <div v-if="error.length > 0" class="alert alert-danger">{{ error }}</div>
            <div class="row row-cols-1 row-cols-md-4 g-4">
                <Card :movie="movie" v-for="movie in movies" :key="movie.id" />
            </div>
        </ul>
    </main>
</template>
