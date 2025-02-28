import "../../styles/UserProfile.css"
import { useContext } from 'react';
import { AuthContext } from '../../contexts/AuthContext.jsx';

const UserProfile = () => {
    const { user, logout } = useContext(AuthContext);

    if (!user) {
        return <div>Loading...</div>;
    }

    return (
        <div class="page-container">
            <h2>User Profile</h2>
            <div class="card">
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
            </div>
            <button class="button" onClick={logout}>Logout</button>
        </div>
    );
};

export default UserProfile;