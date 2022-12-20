import { Setter, createContext, createRoot, createSignal } from "solid-js";

export type AuthType = {
  uid: string | undefined;
  token: string | undefined;
};

const AuthContext = createContext<{
  auth: AuthType;
  setAuth: Setter<AuthType>;
}>();

const createAuth = (props) => {
  const [auth, setAuth] = createSignal<AuthType>(
    props.auth || {
      uid: undefined,
      token: undefined,
    }
  );
  return { auth, setAuth };
};

export default createRoot(createAuth);
