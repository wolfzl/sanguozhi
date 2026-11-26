import { defineConfig } from "astro/config";
import { loadEnv } from "vite";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

// SANGUO_SITE / SANGUO_BASE 可以写在 .env 里，也可以在命令行设置（见 .env.example）。
const env = loadEnv(process.env.NODE_ENV ?? "production", process.cwd(), "");
const site = process.env.SANGUO_SITE || env.SANGUO_SITE || undefined;
// 部署在子路径（如 GitHub 项目页 /sanguozhi/）时设置；默认站点根目录。
const base = (process.env.SANGUO_BASE || env.SANGUO_BASE || "/").replace(/\/?$/, "/");

/**
 * 页面和内容数据里的站内链接都按站点根路径书写（如 /people/caocao/）。
 * 部署在子路径时，构建完成后给生成的 HTML 中这些根路径链接统一加上 base 前缀。
 */
function prefixRootLinks() {
  return {
    name: "prefix-root-links",
    hooks: {
      "astro:build:done": async ({ dir }) => {
        if (base === "/") return;
        const prefix = base.slice(0, -1); // "/sanguozhi"
        const pattern = new RegExp(`(\\s(?:href|src|action|poster)=["'])/(?!/|${prefix.slice(1)}/)`, "g");
        const walk = async (folder) => {
          for (const entry of await fs.readdir(folder, { withFileTypes: true })) {
            const file = path.join(folder, entry.name);
            if (entry.isDirectory()) await walk(file);
            else if (entry.name.endsWith(".html")) {
              const html = await fs.readFile(file, "utf8");
              const next = html.replace(pattern, `$1${base}`);
              if (next !== html) await fs.writeFile(file, next);
            }
          }
        };
        await walk(fileURLToPath(dir));
      },
    },
  };
}

export default defineConfig({
  output: "static",
  trailingSlash: "always",
  devToolbar: { enabled: false },
  site,
  base,
  integrations: [prefixRootLinks()],
});
