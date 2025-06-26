export function initSocket() {
  if (!window.frappe?.socketio?.init) {
    console.warn('⚠️ frappe.socketio.init not found')
    return null
  }

  try {
    frappe.socketio.init()
    return frappe.socketio
  } catch (e) {
    console.error('Socket init error:', e)
    return null
  }
}
