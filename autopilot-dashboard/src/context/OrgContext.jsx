// src/context/OrgContext.jsx

import { createContext, useContext, useEffect, useState } from "react";
import { useAuth } from "./AuthContext";

const OrgContext = createContext();

export function OrgProvider({ children }) {
  const { user } = useAuth();
  const [organization, setOrganization] = useState(null);

  useEffect(() => {
    if (!user?.organizations?.length) return;

    const defaultOrg = user.organizations[0];
    setOrganization(defaultOrg);
    localStorage.setItem("active_org", JSON.stringify(defaultOrg));
  }, [user]);

  return (
    <OrgContext.Provider
      value={{
        organization,
        setOrganization,
      }}
    >
      {children}
    </OrgContext.Provider>
  );
}

export const useOrg = () => useContext(OrgContext);
