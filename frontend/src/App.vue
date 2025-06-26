<template>
  <FrappeUIProvider>
    <Layout>
      <div class="text-base">
        <router-view />
      </div>
    </Layout>
    <Dialogs />
  </FrappeUIProvider>
</template>

<script setup>
import { FrappeUIProvider } from 'frappe-ui'
import { Dialogs } from '@/utils/dialogs'
import { computed, onUnmounted, ref, watch } from 'vue'
import { useScreenSize } from './utils/composables'
import DesktopLayout from '@/components/DesktopLayout.vue'
import MobileLayout from '@/components/MobileLayout.vue'
import NoSidebarLayout from '@/components/NoSidebarLayout.vue'
import { usersStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { posthogSettings } from '@/telemetry'

const screenSize = { width: 1024 } 
const router = useRouter()
const noSidebar = ref(false)
const { userResource } = usersStore()

router.beforeEach((to, from, next) => {
  noSidebar.value = to.query.fromLesson || to.path === '/persona'
  next()
})

const Layout = computed(() => {
  if (noSidebar.value) return NoSidebarLayout
  return screenSize.width < 640 ? MobileLayout : DesktopLayout
})

onUnmounted(() => {
  noSidebar.value = false
})

watch(userResource, () => {
  if (userResource.data) posthogSettings.reload()
})
</script>
