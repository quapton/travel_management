<template>
	<div class="p-4">
		<h2 class="text-xl font-semibold">Trip Detail - {{ tripID }}</h2>
	</div>
</template>

<script setup>
import { usePageMeta } from 'frappe-ui'
import { useRoute } from 'vue-router'

const route = useRoute()
const tripID = route.params.tripID

usePageMeta(() => ({
	title: `Trip - ${tripID}`,
	icon: 'briefcase',
}))
</script>
