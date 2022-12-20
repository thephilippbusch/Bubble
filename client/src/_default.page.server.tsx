// @ts-expect-error
import { generateHydrationScript, renderToStream } from "solid-js/web";
import App from "./App";
import {
  escapeInject,
  dangerouslySkipEscape,
  stampPipe,
} from "vite-plugin-ssr";
import { PageContext } from "./types";
import logoUrl from "./logo.svg";

export { render };
export { passToClient };

// See https://vite-plugin-ssr.com/data-fetching
const passToClient = ["pageProps", "documentProps"];

const render = (pageContext: PageContext) => {
  const { Page, pageProps } = pageContext;

  const { pipe } = renderToStream(() => (
    <App route={() => ({ Page, pageProps })} />
  ));
  stampPipe(pipe, "node-stream");

  // See https://vite-plugin-ssr.com/head
  const { documentProps } = pageContext;
  const title = (documentProps && documentProps.title) || "Vite Solid SSR app";
  const description =
    (documentProps && documentProps.description) || "App using Vite + Solid JS";

  return escapeInject`<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" href="${logoUrl}" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="${description}" />
        <title>${title}</title>
        ${dangerouslySkipEscape(generateHydrationScript())}
      </head>
      <body>
        <div id="page-view">${pipe}</div>
      </body>
    </html>`;
};
