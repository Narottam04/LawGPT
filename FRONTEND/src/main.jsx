import React from "react";
import ReactDOM from "react-dom/client";
// import App from "./App.jsx";
import "./index.css";
import SidebarContextProvider from "./context/SidebarContext.jsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./pages/Login.jsx";
import ChatBot from "./pages/ChatBot.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/app",
    element: <ChatBot />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <SidebarContextProvider>
      {/* <App /> */}
      <RouterProvider router={router} />
    </SidebarContextProvider>
  </React.StrictMode>
);
