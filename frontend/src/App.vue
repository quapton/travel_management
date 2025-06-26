<template>
  <ion-app>
    <FrappeUIProvider>
      <Layout>
        <div class="text-base">
          <router-view />
        </div>
      </Layout>
      <Dialogs />
    </FrappeUIProvider>

    <Toasts />
    <InstallPrompt />
  </ion-app>
</template>

<script setup>
import { onMounted, computed, onUnmounted, ref, watch } from "vue"
import { useRouter } from "vue-router"
import { IonApp } from "@ionic/vue"

import { FrappeUIProvider, Toasts } from "frappe-ui"
import InstallPrompt from "@/components/InstallPrompt.vue"
import { Dialogs } from "@/utils/dialogs"
import { useScreenSize } from "@/utils/composables"
import { usersStore } from "@/stores/user"
import { posthogSettings } from "@/telemetry"
import DesktopLayout from "@/components/DesktopLayout.vue"
import MobileLayout from "@/components/MobileLayout.vue"
import NoSidebarLayout from "@/components/NoSidebarLayout.vue"
import { showNotification } from "@/utils/pushNotifications"

const screenSize = useScreenSize()
const router = useRouter()
const noSidebar = ref(false)
const { userResource } = usersStore()

router.beforeEach((to, from, next) => {
  if (to.query.fromLesson || to.path === '/persona') {
    noSidebar.value = true
  } else {
    noSidebar.value = false
  }
  next()
})

const Layout = computed(() => {
  if (noSidebar.value) {
    return NoSidebarLayout
  }
  if (screenSize.width < 640) {
    return MobileLayout
  }

  return DesktopLayout
})

onUnmounted(() => {
  noSidebar.value = false
})

watch(userResource, () => {
  if (userResource.data) {
    posthogSettings.reload()
  }
})

onMounted(() => {
  window?.frappePushNotification?.onMessage((payload) => {
    showNotification(payload)
  })
})
</script>
