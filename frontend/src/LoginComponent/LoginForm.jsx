import React from 'react'
import {LoginAdminStatus} from "../App";
import axios from 'axios';

export default function LoginForm() {
  const {setUserStatus}=React.useContext(LoginAdminStatus);
   const [state,dispatch]=React.useReducer({
    email:'',
    password:''
   });

  const handleLoginSubmit=()=>{
         try{
         const response=axios.post("http://127.0.0.1:5000/login",{
              headers:{
                   'content-type':'multipart/form-data'
              }

         });
         setUserStatus(response.data);

         }catch(error){
             console.log(error)
         }
  }
  return (
    <div>

       
    </div>
  )
}
