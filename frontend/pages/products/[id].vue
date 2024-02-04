<template>
    <div>
        <p>Product details for {{ id }}</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi, minima, voluptatum delectus sequi assumenda illum
            error quas vero corporis necessitatibus ipsa consequatur nisi! Tenetur magni repellat delectus, eum earum
            recusandae.</p>

    </div>
</template>

<script setup>
const { id } = useRoute().params

definePageMeta({
    layout: "products"
})

</script>

<style scoped>
h2 {

    margin-bottom: 20px;
    font-size: 36px;
}

p {
    margin: 20px 0;

}
</style>