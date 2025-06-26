import { defineStore } from 'pinia'
import { createResource } from 'frappe-ui'

export const sessionStore = defineStore('session', () => {
	const isLoggedIn = window.frappe?.session?.user !== 'Guest'

	const sessionUser = createResource({
		url: 'frappe.client.get_value',
		params: {
			doctype: 'User',
			fieldname: ['name', 'email'],
			filters: { name: window.frappe?.session?.user },
		},
		auto: isLoggedIn,
	})

	const brand = {
		favicon: '/assets/travel_management/images/travel.png',
		logo: '/assets/travel_management/images/logo.svg',
	}

	return {
		isLoggedIn,
		sessionUser,
		brand,
	}
})
