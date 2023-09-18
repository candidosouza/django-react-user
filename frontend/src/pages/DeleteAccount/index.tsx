import React, { useEffect } from 'react';
import http from '../../http';
import { useNavigate } from 'react-router-dom';
import jwt_decode from 'jwt-decode';
import { useAuth } from '../../contexts/AuthContext';

export default function DeleteAccount() {
  const navigate = useNavigate();
  const { isAuthenticated, logout } = useAuth();

  useEffect(() => {
    const deleteAccount = async () => {
      try {
        // const token = localStorage.getItem('accessToken');
        const token = sessionStorage.getItem('accessToken');
        if (!token) {
          navigate('/');
          return;
        }
        const decoded: any = jwt_decode<{
          user_id: string,
          user_fullname: string,
          user_email: string,
          user_password: string
        }>(token);

        await http.delete(`api/users/${decoded.user_id}`)
          .then(response => {
            console.log('Account deleted:', response.data);
          })
          .catch(error => {
            console.error('Error deleting account:', error);
          });
      } catch (error) {
        console.error('Error deleting account:', error);
      }
    };
    deleteAccount();
    // localStorage.removeItem('token');
    sessionStorage.removeItem('accessToken');
    logout();
    navigate('/');
  }, [isAuthenticated, logout, navigate]);
  return null;
}
