<template>

    <div
        v-if="displayFlash"
        v-bind:class="[isSuccess ? alertSuccessClass : alertErrorClass]"
        class="alert">
        {{ flashMessage }}
    </div>
    
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

    // flash elements
    let flashMessage = ref("");
    let displayFlash = ref(false);
    let isSuccess = ref(false);
    let alertSuccessClass = ref("alert-success");
    let alertErrorClass = ref("alert-danger");


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

    function clearFormFields() {
        title.value = "";
        description.value = "";
        poster.value = "";
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
      console.log(data);
      if ("errors" in data) {
        flashMessage.value = [...data.errors];
        isSuccess.value = false;
        displayFlash.value = true;
        } 
      else {
        displayFlash.value = true;
        isSuccess.value = true;
        flashMessage.value = "Movie added successfully!";
        clearFormFields();
        console.log(data);
        }
        
        })
        .catch(function (error) {
            // console.log("Something")
            console.log(error);
        });
    }
</script>