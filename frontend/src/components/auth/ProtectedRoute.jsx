import { useContext } from "react";
import PropTypes from "prop-types";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../../contexts/AuthContext";

const ProtectedRoute = ({ children }) => {
  const { user } = useContext(AuthContext);

  if (!user) {
    return <Navigate to="/login" />;
  }

  return children;
};


// Add PropTypes validation
ProtectedRoute.propTypes = {
  children: PropTypes.node.isRequired,
};


export default ProtectedRoute;
