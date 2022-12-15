import { Component, createSignal, onCleanup, onMount } from "solid-js";

const App: Component = () => {
  const [counter, setCounter] = createSignal(100);

  onMount(() => {
    const interval = setInterval(() => {
      setCounter((prevCount) => prevCount - 1);
    }, 1000);

    onCleanup(() => clearInterval(interval));
  });

  console.log(import.meta.env.CLIENT_PORT);

  return (
    <div class="flex h-screen w-screen flex-col items-center justify-center overflow-y-auto bg-[url('/patterns/underwater-ocean-background-pattern.png')] bg-contain bg-repeat">
      <div class="flex w-full max-w-lg flex-col items-center space-y-2 rounded-xl bg-slate-300 p-4">
        <p class="text-2xl text-indigo-900">Hello Bubble!</p>

        <p class="text-indigo-900">
          Counting all the way from the top: {counter()}
        </p>
      </div>
    </div>
  );
};

export default App;
