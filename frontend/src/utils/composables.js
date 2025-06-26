import { reactive, onMounted } from 'vue'

export function useScreenSize() {
  const screenSize = reactive({
    width: window.innerWidth,
    height: window.innerHeight
  })

  onMounted(() => {
    window.addEventListener('resize', () => {
      screenSize.width = window.innerWidth
      screenSize.height = window.innerHeight
    })
  })

  return screenSize
}
