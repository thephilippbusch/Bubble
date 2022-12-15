import { defineConfig, loadEnv } from "vite";
import solidPlugin from "vite-plugin-solid";

/** @type {import('vite').UserConfig} */
export default defineConfig(({ command: _, mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    plugins: [solidPlugin()],
    server: {
      host: true,
      port: parseInt(env.CLIENT_PORT),
    },
    build: {
      target: "esnext",
    },
  };
});
