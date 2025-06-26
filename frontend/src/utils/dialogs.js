import { useDialog } from 'frappe-ui'

export function createDialog(options) {
	return useDialog().open(options)
}