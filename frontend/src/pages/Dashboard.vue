<template>
	<div class="p-4">
		<h1 class="text-2xl font-bold">Travel Dashboard</h1>
		<p>Welcome to the travel management app.</p>
	</div>
</template>

<script setup>
import { usePageMeta } from 'frappe-ui'
usePageMeta(() => ({
	title: 'Dashboard',
	icon: 'plane',
}))
</script>
