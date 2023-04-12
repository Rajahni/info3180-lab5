<script setup>
    import { ref, onMounted } from "vue";
    import Card from "../components/Card.vue";

    let movies = ref([]);

    onMounted(() => {
        fetchMovies();
        
    });

    function fetchMovies() {
        fetch("api/v1/movies", {
            method: "GET"
        })
        .then((resp) => resp.json())
        .then((data) => {
            movies.value = data.data;
        })
        .catch((err) => {
            console.log(err)
            // error.value = "Unable to fetch your movies";
        })
    }

</script>

<template>
    <main class="container py-5">
        <h1 class="display-1 mb-3">Movies</h1>
        <!-- <div class="d-flex justify-content-center"> -->
            <!-- <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div> -->
        <!-- </div> -->

        <ul>
            <!-- <div> 0" class="alert alert-danger">{{ error }}</div> -->
            <div class="row row-cols-1 row-cols-md-4 g-4">
                <Card :movie="movie" v-for="movie in movies" :key="movie.id"/>
            </div>
        </ul>
    </main>
</template>
