<script setup>

const props = defineProps(['movie'])

</script>

<template>
    <div class="col col-md-4">
        <div class="card">
            <img :src="movie.poster" id="movie-poster" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">{{ movie.description }}</h6>
                <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
            </div>
        </div>
    </div>
</template>

<style>
 #movie-poster{
    width: auto;
    height: 300px;
 }
</style>