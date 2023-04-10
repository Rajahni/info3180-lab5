<template>
    <form @submit.prevent="saveMovie" method="post" enctype="multipart/form-data" id="movieForm">
      
        <label for="title" class="form-label">Enter Movie Title:</label>
        <input type="text" name="title" id="title" class="form-control" >

        <label for="description" class="form-label">Description: </label>
        <textarea name="description" id="description" class="form-control" cols="30" rows="5" ></textarea>

        <label for="poster" class="form-label">Upload Poster: </label>
        <input type="file" name="poster" id="poster" class="form-control" >
        
        <button type="submit">Submit Movie</button>
        
    </form>
</template>

<script setup>

    import { ref, onMounted } from "vue";
    let csrf_token = ref("");

    onMounted(() => {
        getCsrfToken();
    });

    
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }

    function saveMovie() {
        let movieForm = document.getElementById("movieForm");
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message
            console.log(data);
        })
        .catch(function (error) {
            // console.log("Something")
            console.log(error);
        });
    }
</script>