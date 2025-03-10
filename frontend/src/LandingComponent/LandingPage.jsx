import React from 'react'
import Registration from '../Registration/Registration';
import LoginForm from '../LoginComponent/LoginForm';
export default function LandingPage() {

    const [status,setStatus]=React.useState(true);

  return (
    <div>
    
         <div
         onClick={()=>setStatus(prev=>!prev)}
         >{status?'Login':'Registration'}</div>

        {status && <Registration/>}
        {!status && <LoginForm/>}
    </div>
  )
}
