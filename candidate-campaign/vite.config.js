import { defineConfig } from "vite";

export default defineConfig({
  root: "webllm",
  base: "./",
  build: {
    outDir: "../assets/webllm",
    emptyOutDir: true,
  },
});
