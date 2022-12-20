import authContext from "../context/authContext";

export enum Method {
  POST = "POST",
  PUT = "PUT",
  DELETE = "DELETE",
}

type ReturnTypeBase<ReturnType> = {
  successful: boolean;
  data?: ReturnType;
  error?: string;
};

export const mutate = async <PayloadType, ReturnType>({
  url,
  payload,
  method,
}: {
  url: string;
  payload: PayloadType;
  method: Method;
}): Promise<ReturnTypeBase<ReturnType>> => {
  const { auth } = authContext;

  const res = await fetch(
    `${import.meta.env.VITE_SERVER_URL ?? "http://localhost:4000"}${url}`,
    {
      method: method,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth().token}`,
      },
      body: JSON.stringify(payload),
    }
  );

  const data = await res.json();
  return data as ReturnTypeBase<ReturnType>;
};

export const query = async <ReturnType>(
  url: string
): Promise<ReturnTypeBase<ReturnType>> => {
  const { auth } = authContext;

  const res = await fetch(
    `${import.meta.env.VITE_SERVER_URL ?? "http://localhost:4000"}${url}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${auth().token}`,
      },
    }
  );

  const data = await res.json();
  return data as ReturnTypeBase<ReturnType>;
};
