export const clientRouting = true;
export { render };

import { createSignal } from "solid-js";
import { hydrate } from "solid-js/web";
import type { PageContextBuiltInClient } from "vite-plugin-ssr/client/router";
import App from "./App";
import type { Route } from "./Navigation";
import type { PageContext } from "./types";

let layoutReady = false;

// Central signal to track the current active route.
const [route, setRoute] = createSignal<Route | null>(null);

const render = (pageContext: PageContextBuiltInClient & PageContext) => {
  const content = document.getElementById("page-view");
  const { Page, pageProps } = pageContext;

  // Set the new route.
  setRoute({ Page, pageProps });

  // If haven't rendered the layout yet, do so now.
  if (!layoutReady) {
    // Render the page.
    // This is the first page rendering; the page has been rendered to HTML
    // and we now make it interactive.
    hydrate(() => <App route={() => route()} />, content!);
    layoutReady = true;
  }
};
