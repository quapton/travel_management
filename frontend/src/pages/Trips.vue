<template>
	<div class="p-4">
		<h2 class="text-xl font-semibold mb-4">My Trips</h2>
		<!-- Render list of trips -->
	</div>
</template>

<script setup>
import { usePageMeta } from 'frappe-ui'
usePageMeta(() => ({
	title: 'Trips',
	icon: 'map',
}))
</script>
