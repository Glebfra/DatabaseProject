import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import axios from "axios";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Login from "./modules/auth/Login";
import CheckAuth from "./modules/auth/CheckAuth";
import Account from "./modules/account/Account";

axios.defaults.baseURL = 'http://api.localhost/'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <BrowserRouter basename='/'>
            <Routes>
                <Route
                    path='/'
                    element={<App/>}
                />

                <Route
                    path='/login'
                    element={<Login/>}
                />

                <Route
                    path='/account'
                    element={
                        <CheckAuth redirectTo='/login'>
                            <Account/>
                        </CheckAuth>
                    }
                />
            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
