import compression from "compression";
import express from "express";
import { renderPage } from "vite-plugin-ssr";

const isProduction = process.env.NODE_ENV === "production";
const root = `${__dirname}/..`;

startServer();

async function startServer() {
  const app = express();

  app.use(compression());

  if (isProduction) {
    const sirv = require("sirv");
    app.use(sirv(`${root}/dist/client`));
  } else {
    const vite = require("vite");
    const viteDevMiddleware = (
      await vite.createServer({
        root,
        server: { middlewareMode: true },
      })
    ).middlewares;
    app.use(viteDevMiddleware);
  }

  app.get("*", async (req, res, next) => {
    const pageContextInit = {
      urlOriginal: req.originalUrl,
    };
    const pageContext = await renderPage(pageContextInit);
    const { httpResponse } = pageContext;
    if (!httpResponse) return next();
    const { body, statusCode, contentType, earlyHints } = httpResponse;
    if (res.writeEarlyHints)
      res.writeEarlyHints({ link: earlyHints.map((e) => e.earlyHintLink) });
    res.status(statusCode).type(contentType).send(body);
  });

  const port = process.env.CLIENT_PORT || 8080;
  app.listen(port);
  console.log(`Server running at http://localhost:${port}`);
}
