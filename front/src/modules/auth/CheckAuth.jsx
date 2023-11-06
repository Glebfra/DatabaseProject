import {Navigate} from "react-router-dom";
import axios from "axios";

export default ({children, redirectTo}) => {
    return localStorage.getItem('access') ? children : <Navigate to={redirectTo}/>;
}
