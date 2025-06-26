<template>
	<div class="p-4">
		<h2 class="text-xl font-semibold">Settings</h2>
	</div>
</template>

<script setup>
import { usePageMeta } from 'frappe-ui'
usePageMeta(() => ({
	title: 'Settings',
	icon: 'settings',
}))
</script>
