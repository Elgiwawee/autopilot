// src/components/layout/TopNav.jsx

import { User, Globe } from "lucide-react";
import { useAuth } from "../../context/AuthContext";

export default function TopNav() {
  const { user } = useAuth();

  return (
    <div className="h-14 border-b border-border bg-panel flex items-center justify-between px-8">
      
      <div className="font-semibold text-lg">
        AI Cloud Autopilot
      </div>

      <div className="flex items-center gap-6 text-sm text-muted">
        
        <div className="flex items-center gap-2">
          <Globe size={16} />
          us-east-1
        </div>

        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-xs font-semibold text-black">
            {user?.email?.charAt(0).toUpperCase()}
          </div>
          {user?.email}
        </div>

      </div>
    </div>
  );
}