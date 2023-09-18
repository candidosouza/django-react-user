import { Routes, Route } from 'react-router-dom';
import { AuthProvider } from '../contexts/AuthContext';
import Home from './Home';
import AutoLogout from './AutoLogout';
import Update from './Update';
import DeleteAccount from './DeleteAccount';

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/update/:id?" element={<Update />} />
        <Route path="/delete" element={<DeleteAccount />} />
        <Route path="/logout" element={<AutoLogout />} />
      </Routes>
    </AuthProvider>
  );
}
