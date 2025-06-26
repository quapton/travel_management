import { defineStore } from 'pinia'
import { createResource } from 'frappe-ui'

export const useSettings = defineStore('settings', () => {
	const allowGuestAccess = createResource({
		url: 'frappe.client.get_value',
		params: {
			doctype: 'System Settings',
			fieldname: 'allow_guest_access',
		},
		auto: true,
	})

	return { allowGuestAccess }
})
