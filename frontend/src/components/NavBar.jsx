import { Link } from "react-router-dom";
import "../styles/NavBar.css"

function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">FARM ToDo App</Link>
      </div>
      <div className="navbar-links">
        {/* <Link to="/" className="nav-link">
          Home
        </Link> */}
        <Link to="/Dashboard" className="nav-link">
          Dashboard
        </Link>
        <Link to="/Register" className="nav-link">
          Register
        </Link>
        <Link to="/Profile" className="nav-link">
          Profile
        </Link>
      </div>
    </nav>
  );
}

export default NavBar;