<template>
    <section class="section-hero section-shaped my-0">
        <div class="shape shape-style-1 shape-primary">
            <span class="span-150"></span>
            <span class="span-50"></span>
            <span class="span-50"></span>
            <span class="span-75"></span>
            <span class="span-100"></span>
            <span class="span-75"></span>
            <span class="span-50"></span>
            <span class="span-100"></span>
            <span class="span-50"></span>
            <span class="span-100"></span>
        </div>
        <div class="container shape-container d-flex align-items-center">
            <div class="col px-0">
                <div class="row justify-content-center align-items-center">
                    <!-- <div class="col-lg-7 text-center pt-lg"> -->
                    <div class="col-lg-7 text-center">
                        <img src="img/brand/rakeai.png" style="width: 200px;" class="img-fluid">
                        <p class="h2 text-white mt-4 mb-5">RakeAI，拥抱你的学术梦想   </p>
                        <Productbuttons></Productbuttons>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import Productbuttons from "./new_components/Productbuttons.vue";
export default {
    name: "homepage",
    components: {
        Productbuttons,
    }
};
</script>
