import { defineConfig } from "astro/config";
export default defineConfig({
  output: "static",
  trailingSlash: "always",
  devToolbar: { enabled: false },
  site: process.env.SANGUO_SITE || undefined,
});
