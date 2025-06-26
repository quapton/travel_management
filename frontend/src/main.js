import './index.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

import dayjs from '@/utils/dayjs'
import { createDialog } from '@/utils/dialogs'
import translationPlugin from './translation'
import { usersStore } from './stores/user'
import { initSocket } from './socket'

import {
  FrappeUI,
  setConfig,
  frappeRequest,
  pageMetaPlugin,
} from 'frappe-ui'

const pinia = createPinia()
const app = createApp(App)

// Set global config for frappe-ui resource fetching
setConfig('resourceFetcher', frappeRequest)

// Install plugins
app.use(FrappeUI)
app.use(pinia)
app.use(router)
app.use(translationPlugin)
app.use(pageMetaPlugin)

// Provide utilities globally
app.provide('$dayjs', dayjs)
app.provide('$socket', initSocket())

// Provide user and all users as global resources
const { userResource, allUsers } = usersStore()
app.provide('$user', userResource)
app.provide('$allUsers', allUsers)

// Set global properties for template access
app.config.globalProperties.$user = userResource
app.config.globalProperties.$dialog = createDialog

// Mount app
app.mount('#app')
