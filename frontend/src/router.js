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
		path: '/settings',
		name: 'Settings',
		component: () => import('@/pages/Settings.vue'),
	},
]

const router = createRouter({
	history: createWebHistory('/travel_management'),
	routes,
})

router.beforeEach(async (to, from, next) => {
	const { userResource } = usersStore()
	let { isLoggedIn } = sessionStore()
	const { allowGuestAccess } = useSettings()

	try {
		if (isLoggedIn) {
			await userResource.promise
		}
	} catch {
		isLoggedIn = false
	}

	if (!isLoggedIn) {
		await allowGuestAccess.promise
		if (!allowGuestAccess.data) {
			window.location.href = '/login'
			return
		}
	}

	return next()
})

export default router
