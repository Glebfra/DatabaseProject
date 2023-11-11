import {Navigate} from "react-router-dom";


const redirect = ({children, redirectTo}) => {
    return localStorage.getItem('access') ? children : <Navigate to={redirectTo}/>;
}

export default redirect;
