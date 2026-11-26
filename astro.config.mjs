import { defineConfig } from "astro/config";
import { loadEnv } from "vite";

// SANGUO_SITE 可以写在 .env 里，也可以在命令行设置（见 .env.example）。
const { SANGUO_SITE } = loadEnv(process.env.NODE_ENV ?? "production", process.cwd(), "");

export default defineConfig({
  output: "static",
  trailingSlash: "always",
  devToolbar: { enabled: false },
  site: process.env.SANGUO_SITE || SANGUO_SITE || undefined,
});
