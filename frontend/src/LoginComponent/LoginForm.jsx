import React from 'react'
// import {LoginAdminStatus} from "../App";
import axios from 'axios';
import {useNavigate} from "react-router-dom";
import { LoginAdminStatus } from '../App';
function reducer(state,action){
      switch(action.type){
           case 'email': return {
               ...state,
               email:action.nextEmail
           }

           case 'password':return {
              ...state,
              password:action.nextPassword
           }

           default: return state 
              
      } 
}
export default function LoginForm() {
  // const {setUserStatus}=React.useContext(LoginAdminStatus);
   const [state,dispatch]=React.useReducer(reducer,{
    email:'',
    password:''
   });
   const navigate=useNavigate();

    const [status,setStatus]=React.useState(LoginAdminStatus);
  

  const handleLoginSubmit=async(e)=>{
    e.preventDefault();
    const form=new FormData();
    form.append('email',state.email)
    form.append('password',state.password)
         try{
         const response=await axios.post("http://127.0.0.1:5000/login",form,{
              headers:{
                   'Content-type':'multipart/form-data'
              }

         });
         let data=response.data;
         
          setStatus(data)
         
         }catch(error){
             console.log(error)
         }
  }


  React.useEffect(()=>{
       if(status==='ok'){
            navigate("/profile")
       }else{
        navigate("/")
       }
  },[status,navigate])
  return (
    <div>

    <form onSubmit={handleLoginSubmit}>
      <label>
        Email: 
      </label>
    <input type="email" name="email" value={state.email} 
      onChange={(e)=>dispatch({
          type:'email',
          nextEmail:e.target.value
      })}
      required
    />
    <br></br>
    <label>Password: </label>
    <input 
    type="password" 
    name="password"
    value={state.password}
    onChange={(e)=>dispatch({
        type:'password',
        nextPassword:e.target.value
    })}
    required
    />
      
      <input type='submit' value='Submit'/>
    </form>
   


    {status==='emailInvalid' && <p>Email Does not exist</p>}
  
    {status==='invalidPassword' && <p>Invalid Login</p>}
       
    </div>
  )
}
