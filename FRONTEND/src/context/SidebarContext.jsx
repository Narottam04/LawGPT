import { createContext, useContext, useState } from "react";

// create a context with a placeholder value initially
const SidebarContext = createContext();

// custom hook
export const useSidebar = () => useContext(SidebarContext);

export default function SidebarContextProvider({ children }) {
  const [queryType, setQueryType] = useState("Know Your Rights");
  const [hide, setHide] = useState(true);

  const value = {
    queryType,
    setQueryType,
    hide,
    setHide,
  };

  return (
    <SidebarContext.Provider value={value}>{children}</SidebarContext.Provider>
  );
}
