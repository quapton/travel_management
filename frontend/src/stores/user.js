import { defineStore } from 'pinia'
import { createResource } from 'frappe-ui'

export const usersStore = defineStore('users', () => {
	const userResource = createResource({
		url: 'frappe.client.get_value',
		params: {
			doctype: 'User',
			fieldname: 'full_name',
			filters: { name: 'frappe.session.user' },
		},
		auto: true,
	})

	const allUsers = createResource({
		url: 'frappe.client.get_list',
		params: {
			doctype: 'User',
			fields: ['name', 'full_name', 'email'],
		},
		auto: true,
	})

	return { userResource, allUsers }
})
