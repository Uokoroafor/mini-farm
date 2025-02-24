/// <reference types="vitest" />
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()], // Enables automatic React import like in Vite
  test: {
    environment: "jsdom",
    setupFiles: "./src/setupTests.jsx",
  },
});

