<template>
	<div class="p-4">
		<h2 class="text-xl font-semibold">Bookings</h2>
	</div>
</template>

<script setup>
import { usePageMeta } from 'frappe-ui'
usePageMeta(() => ({
	title: 'Bookings',
	icon: 'calendar',
}))
</script>
