
// "use client";

// import { useState, useRef, useEffect } from "react";
// import Link from "next/link";
// import { useRouter } from "next/navigation";
// import { useAuth } from "@/lib/contexts/AuthContext";

// export function UserMenu() {
//   const { user, logout, isAuthenticated } = useAuth();
//   const [isOpen, setIsOpen] = useState(false);
//   const menuRef = useRef<HTMLDivElement>(null);
//   const router = useRouter();

//   useEffect(() => {
//     function handleClickOutside(event: MouseEvent) {
//       if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
//         setIsOpen(false);
//       }
//     }

//     document.addEventListener("mousedown", handleClickOutside);
//     return () => document.removeEventListener("mousedown", handleClickOutside);
//   }, []);

//   const handleLogout = () => {
//     logout();
//     setIsOpen(false);
//     router.push("/auth/login");
//   };

//   if (!isAuthenticated) {
//     return (
//       <div className="flex items-center gap-3">
//         <Link href="/auth/login">
//           <button className="px-4 py-2 text-gray-700 hover:text-blue-600 font-medium transition-colors">
//             Sign In
//           </button>
//         </Link>
//         <Link href="/auth/signup">
//           <button className="px-5 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-full hover:shadow-lg transition-all font-medium">
//             Sign Up
//           </button>
//         </Link>
//       </div>
//     );
//   }

//   return (
//     <div className="relative" ref={menuRef}>
//       <button
//         onClick={() => setIsOpen(!isOpen)}
//         className="flex items-center gap-3 px-4 py-2 rounded-full hover:bg-gray-100 transition-colors"
//       >
//         <div className="w-8 h-8 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 flex items-center justify-center text-white font-semibold text-sm">
//           {user?.name?.charAt(0).toUpperCase() || "U"}
//         </div>
//         <span className="text-sm font-medium text-gray-700 hidden sm:inline">
//           {user?.name}
//         </span>
//       </button>

//       {isOpen && (
//         <div className="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50">
//           <div className="px-4 py-3 border-b border-gray-100">
//             <p className="text-sm font-medium text-gray-900">{user?.name}</p>
//             <p className="text-xs text-gray-500">{user?.email}</p>
//           </div>
//           <Link
//             href="/dashboard"
//             className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-blue-600 transition-colors"
//           >
//             Dashboard
//           </Link>
//           <button
//             onClick={handleLogout}
//             className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-red-600 transition-colors"
//           >
//             Sign Out
//           </button>
//         </div>
//       )}
//     </div>
//   );
// }
"use client";

import { useState, useRef, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/contexts/AuthContext";
import { ChevronDown, LogOut, LayoutDashboard } from "lucide-react";

export function UserMenu() {
  const { user, logout, isAuthenticated } = useAuth();
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const router = useRouter();

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);

  }, []);

  const handleLogout = () => {
    logout();
    setIsOpen(false);
    router.push("/auth/login");

  };

  if (!isAuthenticated) {
    return (
      <div className="flex items-center gap-3">
        <Link href="/auth/login">
          <button className="px-5 py-2.5 text-gray-700 hover:text-blue-600 font-semibold transition-all duration-200 hover:bg-blue-50 rounded-full">

            Sign In
          </button>
        </Link>
        <Link href="/auth/signup">

          <button className="px-6 py-2.5 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-full hover:shadow-xl hover:shadow-blue-500/30 hover:-translate-y-0.5 transition-all duration-200 font-semibold">

            Sign Up
          </button>
        </Link>
      </div>
    );
  }

  return (
    <div className="relative" ref={menuRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-3 px-4 py-2.5 rounded-full hover:bg-gray-100 transition-all duration-200 group"
      >
        <div className="w-9 h-9 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white font-bold text-sm shadow-md group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-200">
          {user?.name?.charAt(0).toUpperCase() || "U"}
        </div>
        <div className="flex flex-col items-start hidden sm:block">
          {/* <span className="text-sm font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">
            {user?.name}
          </span> */}
          {/* <span className="text-xs text-gray-500">
            {user?.email?.split("@")[0]}
          </span> */}
        </div>
        <ChevronDown 
          className={`w-4 h-4 text-gray-500 transition-transform duration-200 ${isOpen ? "rotate-180" : ""}`} 
        />
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-56 bg-white rounded-xl shadow-xl border border-gray-100 z-50 overflow-hidden">
          <div className="px-5 py-4 bg-gradient-to-br from-blue-50 to-indigo-50 border-b border-gray-100">
            <div className="flex items-center gap-3">
              {/* <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white font-bold text-sm shadow-md">
                {user?.name?.charAt(0).toUpperCase() || "U"}
              </div> */}
              <div className="flex flex-col">
                <p className="text-sm font-bold text-gray-900">{user?.name}</p>
                <p className="text-xs text-gray-600">{user?.email}</p>
              </div>
            </div>
          </div>
          <div className="py-2">
            <Link
              href="/dashboard"
              className="flex items-center gap-3 px-5 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors"
              onClick={() => setIsOpen(false)}
            >
              <LayoutDashboard className="w-4 h-4" />
              <span className="font-medium">Dashboard</span>
            </Link>
            <button
              onClick={handleLogout}
              className="w-full flex items-center gap-3 px-5 py-3 text-sm text-gray-700 hover:bg-red-50 hover:text-red-600 transition-colors"
            >
              <LogOut className="w-4 h-4" />
              <span className="font-medium">Sign Out</span>
            </button>
          </div>

        </div>
      )}
    </div>
  );

}

