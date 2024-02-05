<template>
    <div class="flex">
        <aside class="container w-1/6 h-screen bg-white pt-6 justify-center text-lg">
            <NuxtLink to="/" class="font-bold">Nuxt Dojo</NuxtLink>
            <ul class="mt-12  px-10  ">
                <li>
                    <NuxtLink to="/">Dashboard</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/about">About</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/products" class="btn">Products</NuxtLink>
                </li>
            </ul>
        </aside>

        <!-- Output page content -->
        <div class="flex-1 bg-white container w-5/6 h-screen mt-4 mx-auto p-4 border-gray-200 border-[2px] rounded-3xl">
            <slot />
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.router-link-exact-active {
    color: #2d8acc;
    background: #000;

}
</style>