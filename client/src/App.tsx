import { Accessor, Component } from "solid-js";
import { Navigation, Route } from "./Navigation";
import "./app.css";

interface Props {
  route: Accessor<Route | null>;
}

const App: Component<Props> = (props) => {
  return <Navigation route={props.route} />;
};

export default App;
