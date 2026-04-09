<script setup lang="ts">

</script>

<template>
  <div class="tgpy-code-block">
    <slot/>
  </div>
</template>

<style scoped>
.tgpy-code-block {
  background-color: var(--vp-c-bg-elv);
  border-radius: 8px;
}

.tgpy-code-block > :deep(div:first-child) {
  margin-bottom: 2px;
}

.tgpy-code-block > :deep(div:last-child) {
  background-color: transparent;
}

.tgpy-code-block > :deep(div:last-child) code {
  color: var(--vp-c-text-1);
}

.tgpy-code-block > :deep(div:last-child) code::before {
  content: 'TGPy> ';
  color: var(--vp-c-text-2);
}
</style>