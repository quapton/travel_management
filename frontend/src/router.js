import { createRouter, createWebHistory } from 'vue-router'
import { usersStore } from './stores/user'
import { sessionStore } from './stores/session'
import { useSettings } from './stores/settings'

const routes = [
	{
		path: '/',
		name: 'Dashboard',
		component: () => import('@/pages/Dashboard.vue'),
	},
	{
		path: '/trips',
		name: 'Trips',
		component: () => import('@/pages/Trips.vue'),
	},
	{
		path: '/trips/:tripID',
		name: 'TripDetail',
		component: () => import('@/pages/TripDetail.vue'),
		props: true,
	},
	{
		path: '/bookings',
		name: 'Bookings',
		component: () => import('@/pages/Bookings.vue'),
	},
	{
