import { defineConfig, loadEnv } from "vite";
import solidPlugin from "vite-plugin-solid";
import ssr from "vite-plugin-ssr/plugin";

/** @type {import('vite').UserConfig} */
export default defineConfig(({ command: _, mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    plugins: [solidPlugin({ ssr: true }), ssr()],
    server: {
      host: true,
      port: parseInt(env.CLIENT_PORT),
      watch: {
        usePolling: true,
      },
    },
    hmr: parseInt(env.CLIENT_PORT),
    build: {
      target: "esnext",
    },
  };
});
