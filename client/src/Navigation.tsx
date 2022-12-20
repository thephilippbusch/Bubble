import { Accessor, JSX, Component, Switch, Match } from "solid-js";
import authContext from "./context/authContext";
import { Login } from "./pages/Login";

export { Navigation };

export interface Route {
  Page: Component;
  pageProps: Record<string, unknown>;
}

interface Props {
  route: Accessor<Route | null>;
}
interface Children {
  children: JSX.Element;
}

const Navigation: Component<Props> = (props) => {
  const { auth } = authContext;

  const renderedRoute = () => {
    const { Page, pageProps } = props.route() ?? {};
    return Page && <Page {...pageProps} />;
  };

  return (
    <Layout>
      <Switch>
        <Match when={!auth().token}>
          <Login />
        </Match>
        <Match when={auth().token}>
          <Sidebar>
            <a class="text-red-500 hover:underline" href="/">
              Home
            </a>
            <a class="text-red-500 hover:underline" href="/about">
              About
            </a>
          </Sidebar>
          <Content>{renderedRoute()}</Content>
        </Match>
      </Switch>
    </Layout>
  );
};

const Layout: Component<Children> = (props) => {
  return <div class="flex h-screen w-screen">{props.children}</div>;
};

const Sidebar: Component<Children> = (props) => {
  return <div class="flex h-full w-36 flex-col p-5">{props.children}</div>;
};

const Content: Component<Children> = (props) => {
  return (
    <div class="h-full border-l border-black p-5 pb-12">{props.children}</div>
  );
};
