import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react';
import axiosInstance from '../api/axiosConfig'
import jwt_decode from 'jwt-decode';


export interface User {
  id: string;
  fullname: string;
  email: string;
  password: string;
}


interface AuthContextData {
  isAuthenticated: boolean;
  user: User | null;
  login: (name: string, email: string, password: string, token: string) => void;
  logout: () => void;
  updateUser: (updatedUser: User) => void;
}

const AuthContext = createContext<AuthContextData | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const token = sessionStorage.getItem('accessToken');
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(token != null);
  const [user, setUser] = useState<{ id: string, fullname: string; email: string; password: string } | null>(null);


  useEffect(() => {
    const token = sessionStorage.getItem('accessToken');
    const userData = sessionStorage.getItem('userData');
  
    if (token && userData) {
      const decoded: any = jwt_decode<{
        user_id: string,
        user_fullname: string,
        user_email: string,
        user_password: string
      }>(token);
  
      const userFromStorage = JSON.parse(userData);
  
      if (decoded) {
        const userId = decoded.user_id;
        setUser({
          id: userId,
          fullname: userFromStorage.fullname,
          email: userFromStorage.email,
          password: userFromStorage.password
        });
        setIsAuthenticated(true);
      }
    }
  }, []);

  const login = (fullname: string, username: string, password: string, token: string) => {
    const decoded: any = jwt_decode<{
      user_id: string,
      user_fullname: string,
      user_email: string,
      user_password: string
    }>(token);
    if (decoded) {
      setIsAuthenticated(true);
      setUser({
        id: decoded.user_id,
        fullname: fullname,
        email: username,
        password: password
      });
      sessionStorage.setItem('accessToken', token);
      sessionStorage.setItem('userData', JSON.stringify({
        id: decoded.user_id,
        fullname: fullname,
        email: username,
        password: password
      }));
      // axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }
  };

  const logout = () => {
    setIsAuthenticated(false);
    setUser(null);
    sessionStorage.removeItem('accessToken');
    sessionStorage.removeItem('userData');
    delete axiosInstance.defaults.headers.common['Authorization'];
  };

  const updateUser = (updatedUser: User) => {
    console.log('updateUser', updatedUser);
    setUser(updatedUser);
    sessionStorage.setItem('userData', JSON.stringify({
      id: updatedUser.id,
      fullname: updatedUser.fullname,
      email: updatedUser.email,
      password: updatedUser.password
    }));
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout, updateUser }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth deve ser usado dentro de um AuthProvider');
  }

  return context;
}
