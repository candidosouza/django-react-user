import { useState, ChangeEvent, FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { Modal } from 'react-bootstrap';
import http from '../../http';

import style from './ModalRegister.module.scss';


interface LoginModalProps {
    show: boolean;
    onClose: () => void;
}

interface FormData {
    fullname: string;
    username: string;
    password: string;
}


export default function RegisterModal({ show, onClose }: LoginModalProps) {
    const navigate = useNavigate();
    const { login } = useAuth();
    // const token = localStorage.getItem('accessToken');
    const token = sessionStorage.getItem('accessToken');

    const [formData, setFormData] = useState<FormData>({
        fullname: '',
        username: '',
        password: '',
    });

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            await http.post('api/users/', formData)
                .then(async response => {
                    setFormData({ ...formData, fullname: '', username: '', password: '' });
                    await http.post('api/token/', formData)
                        .then(response => {
                            login(formData.fullname, formData.username, formData.password, response.data.access);
                            navigate("/");
                        });
                })
                .catch(error => {
                    console.error('Error token:', error);
                });
        } catch (error) {
            console.error('Error logging in:', error);
        }
    };

    return (
        <Modal show={show} onHide={onClose}>
            <Modal.Header closeButton>
                <Modal.Title>Login</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <div className={style.loginform}>
                    <form onSubmit={handleSubmit} className={style.registerform}>
                        <label htmlFor="name">Nome</label>
                        <input type="text" name="fullname" placeholder="Nome" onChange={handleChange} />
                        <label htmlFor="Email">Email</label>
                        <input type="email" name="username" placeholder="Email" onChange={handleChange} />
                        <label htmlFor="Password">Password</label>
                        <input type="password" name="password" placeholder="Password" onChange={handleChange} />
                        <button type="submit">Cadastrar</button>
                    </form>
                </div>

            </Modal.Body>
        </Modal>
    );
}
