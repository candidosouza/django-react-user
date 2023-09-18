import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import style from './Home.module.scss';
import LoginModal from '../../components/ModalLogin';
import RegisterModal from '../../components/ModalRegister';

function maskPassword(password: string): string {
    return '*'.repeat(password.length);
}

export default function Home() {
    const { isAuthenticated, user } = useAuth();
    const [showLoginModal, setShowLoginModal] = useState(false);
    const [showRegisterModal, setShowRegisterModal] = useState(false);
    // const token = localStorage.getItem('accessToken');
    const token = sessionStorage.getItem('accessToken');

    const handleLoginClick = () => {
        setShowLoginModal(true);
    };

    const handleCloseLoginModal = () => {
        setShowLoginModal(false);
    };

    const handleRegisterClick = () => {
        setShowRegisterModal(true);
    };

    const handleCloseRegisterModal = () => {
        setShowRegisterModal(false);
    };

    return (
        <>
            <div className={style.container}>
                <div className={style.jumbotron}>
                    {isAuthenticated ? (
                        <>
                            <h1 className={style.display4}>
                                Bem-vindo!
                            </h1>
                            <p className={style.lead}>
                                Você está logado como {user?.email ?? 'usuário não identificado'}.
                            </p>
                            <p className={style.lead}>
                                senha: Senha: {user ? maskPassword(user.password) : ''}
                            </p>
                            <Link to={`/update/${user?.id}`} className='btn btn-primary'>Alterar Dados</Link>
                            <Link to='/logout' className='btn btn-warning'>Sair</Link>
                            <Link to='/delete' className='btn btn-danger'>Deletar conta</Link>
                        </>
                    ) : (
                        <>
                            <h1 className={style.display4}>Olá!</h1>
                            <p className={style.lead}>Faça o login para ver seus dados.</p>
                            <a onClick={handleLoginClick} className='btn btn-success'>Login</a>
                            <LoginModal show={showLoginModal} onClose={handleCloseLoginModal} />
                            <a onClick={handleRegisterClick} className='btn btn-primary'>Cadastrar Modal</a>
                            <RegisterModal show={showRegisterModal} onClose={handleCloseRegisterModal} />
                        </>
                    )}
                </div>
            </div>
        </>
    );
}
