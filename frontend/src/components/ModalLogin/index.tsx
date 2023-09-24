import { useState, ChangeEvent, FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { Modal } from 'react-bootstrap';
import http from '../../http';

import style from './ModalLogin.module.scss';

interface LoginModalProps {
    show: boolean;
    onClose: () => void;
}

interface FormData {
    username: string;
    password: string;
}


export default function LoginModal({ show, onClose }: LoginModalProps) {
    const navigate = useNavigate();
    const { login } = useAuth();

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
        await http.post('api/token/', formData)
            .then(response => {
                setFormData({ ...formData, username: '', password: '' })
                login(response.data.user_fullname, response.data.user_email, formData.password, response.data.access);
                navigate("/");
            })
            .catch(error => {
                console.error('Error token:', error);
            });
    };

    const isFormEmpty = !formData.username.trim() || !formData.password.trim();

    return (
        <Modal show={show} onHide={onClose}>
            <Modal.Header closeButton>
                <Modal.Title>Login</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <div className={style.loginform}>
                    <form onSubmit={handleSubmit}>
                        <input type="email" name="username" placeholder="Email" onChange={handleChange} required />
                        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
                        <button type="submit" className='btn btn-info' disabled={isFormEmpty}>Login</button>
                    </form>
                </div>

            </Modal.Body>
        </Modal>
    );
}

