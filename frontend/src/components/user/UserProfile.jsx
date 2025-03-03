import "../../styles/UserProfile.css"
import { useContext } from 'react';
import { AuthContext } from '../../contexts/AuthContext.jsx';

const UserProfile = () => {
    const { user, logout } = useContext(AuthContext);

    if (!user) {
        return <div>Loading...</div>;
    }

    return (
        <div className="page-container">
            <h2>User Profile</h2>
            <div className="card">
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
            </div>
            <button className="button" onClick={logout}>Logout</button>
        </div>
    );
};

export default UserProfile;