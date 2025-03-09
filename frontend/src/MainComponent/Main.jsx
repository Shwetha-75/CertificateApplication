  import React from 'react'
  import"./main.css";
  import { LoginAdminStatus } from '../App';
  import Form from "../Component/Main";
  import { useNavigate } from 'react-router-dom';
  export default function Main() {
    
   const navigate=useNavigate();

    const {setUserStatus}=React.useContext(LoginAdminStatus);

    const handleLogoutFunctionality=()=>{
         setUserStatus(false);
        navigate("/");

    }

    return (
      <div className='flex flex-row p-10'>
        <div className='container main--container'>
            <h1 className='heading--tag text-center'>GENERATE YOUR CERTIFICATE </h1>
            <h3 className="logout---tag" onClick={handleLogoutFunctionality}>Logout</h3>
            <Form/>
        </div>
      </div>  
    )
  }
