import React, { useState, ChangeEvent, FormEvent } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth, User } from '../../contexts/AuthContext';
import http from '../../http';
import jwt_decode from 'jwt-decode';
import style from './Update.module.scss';

interface FormData {
  username: string;
  password: string;
}

export default function Update() {
  const navigate = useNavigate();
  const { isAuthenticated, user, updateUser } = useAuth();
  const token = sessionStorage.getItem('accessToken');

  const [formData, setFormData] = useState<FormData>({
    username: '',
    password: '',
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!user || !user.id) {
      navigate('/');
      return;
    }

    const decoded: any = jwt_decode<{
      user_id: string,
      user_fullname: string,
      user_email: string,
      user_password: string
    }>(token || '');

    const password = formData.password || decoded.user_password;
    await http.patch(`api/users/${user.id}/`, formData)
      .then(response => {
        const { id, fullname, email }: User = response.data;
        const updatedUser: User = {
          id,
          fullname,
          email,
          password,
        };

        updateUser(updatedUser);

        navigate('/');
      })
      .catch(error => {
        console.error('Error updating account:', error);
      });
  };

  return (
    <div className={style.logincontainer}>
      <div className={style.form}>
        <h2>Alterar</h2>
        <form onSubmit={handleSubmit}>
          <input type="email" name="username" placeholder="Email" onChange={handleChange} required />
          <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
          <button type="submit">Alterar</button>
        </form>
        <Link to='/' className='btn btn-link'>Home</Link>
      </div>
    </div>
  );
}
