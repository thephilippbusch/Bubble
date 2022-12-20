import { Component, Show, createSignal } from "solid-js";
import authContext from "../context/authContext";
import { Loader } from "../components/Loader";
import { Method, mutate } from "../util";
import { FiEye, FiEyeOff } from "solid-icons/fi";

type LoginPayload = {
  username: string;
  password: string;
};

export const Login: Component = () => {
  const [error, setError] = createSignal<string | undefined>();
  const [loading, setLoading] = createSignal<boolean>(false);

  const [showPassword, setShowPassword] = createSignal<boolean>(false);

  const { setAuth } = authContext;

  let usernameRef: HTMLInputElement;
  let passwordRef: HTMLInputElement;

  const login = async () => {
    setLoading(true);

    if (!usernameRef.value || usernameRef.value === "") {
      setLoading(false);
      return setError("Please provide a username to login!");
    }

    if (!passwordRef.value || passwordRef.value === "") {
      setLoading(false);
      return setError("Please provide a password to login!");
    }

    const result = await mutate<LoginPayload, { token: string; uid: string }>({
      url: "/auth/sign_in",
      payload: {
        username: usernameRef.value,
        password: passwordRef.value,
      },
      method: Method.POST,
    });

    if (!result.successful) {
      setLoading(false);
      return setError(result.error ?? "Login was unsuccessful!");
    }

    setLoading(false);
    setAuth({
      token: result.data.token,
      uid: result.data.uid,
    });
  };

  return (
    <div
      id="login_page"
      class="flex h-full w-full flex-col items-center justify-center bg-[url('/patterns/underwater-ocean-background-pattern.png')] bg-[length:400px_400px] bg-repeat text-black dark:text-white"
    >
      <div
        id="login_input_container"
        class="flex w-full max-w-md flex-col space-y-2 rounded-lg bg-sky-50 p-4 shadow-xl dark:bg-sky-800 dark:shadow-none"
      >
        <h1
          id="login_title"
          class="mb-2 w-full border-b border-slate-700 pb-2 text-center text-3xl font-bold dark:border-slate-400"
        >
          Login Page
        </h1>

        <input
          id="login_username_input"
          ref={usernameRef}
          type="text"
          class="w-full rounded-md border border-slate-500 bg-transparent py-0.5 px-2 duration-200 ease-in-out hover:border-slate-700 focus:border-blue-800 focus:outline-none dark:border-slate-600 dark:hover:border-slate-400 dark:focus:border-blue-400"
        />

        <div
          id="login_password_wrapper"
          class="flex w-full flex-row items-center space-x-2"
        >
          <input
            id="login_password_input"
            ref={passwordRef}
            type={showPassword() ? "text" : "password"}
            class="flex-1 rounded-md border border-slate-500 bg-transparent py-0.5 px-2 duration-200 ease-in-out hover:border-slate-700 focus:border-blue-800 focus:outline-none dark:border-slate-600 dark:hover:border-slate-400 dark:focus:border-blue-400"
          />
          <button
            id="login_show_password_btn"
            onClick={() => setShowPassword((prevState) => !prevState)}
            class="rounded-md bg-transparent bg-opacity-25 px-2 py-1 duration-200 ease-in-out hover:bg-slate-300 focus:outline-none dark:hover:bg-slate-600"
          >
            {showPassword() ? <FiEyeOff size={25} /> : <FiEye size={25} />}
          </button>
        </div>

        <Show when={error()}>
          <p class="w-full text-center text-sm text-red-400 dark:text-red-600">
            {error()}
          </p>
        </Show>

        <Show when={loading()}>
          <Loader />
        </Show>

        <Show when={!loading()}>
          <button
            id="login_show_password_btn"
            class="self-center rounded-md bg-blue-700 px-3 py-1.5 text-white duration-200 ease-in-out hover:bg-blue-800 focus:outline-none"
            onClick={() => login()}
          >
            Login
          </button>
        </Show>
      </div>
    </div>
  );
};
