import React from 'react'
import axios from "axios";
import { useNavigate, useLocation} from 'react-router-dom';
import RegistrationFail from './RegistrationFail';
import RegistrationSuccess from './RegistrationSuccess';
import { LoginAdminStatus } from '../App';
function reducer(state={
  userName:'',
  email:"",
  linkedInProfile:'',
  gitHubProfile:"",
  password:"",
  confirmPassword:''
},action){
     switch(action.type){
  
           case "userName":return {
            ...state,
            userName:action.nextUserName
           }

           case "email": return {
            ...state,
            email:action.nextEmail
           }

           case "linkedInProfile":return{
            ...state,
            linkedInProfile:action.nextLinkedIn
           }

           case "gitHubProfile":return{
            ...state,
            gitHubProfile:action.nextGitHub
           }
           case "password": return {
            ...state,
            password:action.nextPassword
           }

           case "confirmPassword": return {
               ...state,
               confirmPassword:action.nextConfirmPassword
           }
           default: return state
          }
}
export default function Registration() {
 
  const [password,setPassword]=React.useState([false,'']);
  const {userStatus,setUserStatus}=React.useContext(LoginAdminStatus);
  const navigate=useNavigate();
  const location=useLocation();
  const [userNameStatus,setUserNameStatus]=React.useState('');
  const [formSubmissioon,setFormSubmission]=React.useState("");



  const [state,dispatch]=React.useReducer(reducer,{
    userName:'',
    email:"",
    linkedInProfile:'',
    gitHubProfile:"",
    password:"",
    confirmPassword:''
  })


  const handleOnSubmit=async(e)=>{
   
    e.preventDefault();
    if(!passwordValidation(state.password)[0]){

            setPassword([true,'password criteria is not matching'])
           return;

    }
    if(!passwordConfirmPassword(state.password,state.confirmPassword)){
         setPassword([true,'both confirm password and password are not matching'])
         return; 
    }
    if(userNameStatus==='no'){
      setFormSubmission(true)
      return ;
    }
    setPassword([false,''])
    const form=new FormData();
    form.append("userName",state.userName);
    form.append("email",state.email);
    form.append("linkedInProfile",state.linkedInProfile);
    form.append("gitHubProfile",state.gitHubProfile);
    form.append("password",state.password);
    form.append("confirmPassword",state.confirmPassword);
    console.log(form)
     try{
     const response=await axios.post("http://127.0.0.1:5000/register",form,{
            headers:{
              "Content-type":'multipart/form-data'
            }
     });
     setUserStatus(response.data);     
     setFormSubmission(false);  
     }
     catch(error){
           console.log(error);
     }
  }
  
  React.useEffect(()=>{
    localStorage.setItem('userStatus',JSON.stringify(userStatus));

  });

  React.useEffect(()=>{


    async function userNameValidation(){
     
      if(state.userName.length>5){
        const formData=new FormData();
       
        formData.append('userName',state.userName)
        console.log(formData.get('userName'))
        try{
          const response=await axios.post("http://127.0.0.1:8081/username",formData,{
                headers:{
                    "Content-type":'multipart/form-data'
                  }
                }
                
                
              )  
               console.log(response.data)
               setUserNameStatus(response.data)
              
            }catch(error){
              console.log(error)
            }
          }
        }
   

        userNameValidation();
     
  },[state]);



React.useEffect(()=>{
  if(userStatus==='no'|| userStatus===false){
        navigate("/")
  }
  else{
      navigate("/profile")
  }
},[userStatus,navigate]);

React.useEffect(()=>{
      const handleBrowserBackButton=()=>{
          if(location.pathname==='/'){
              navigate(1);
          }
      }

      window.addEventListener("popstate",handleBrowserBackButton);
      return ()=>window.removeEventListener("popstate",handleBrowserBackButton)
},[userStatus,navigate,location ])



  return (
    <div>
      <form onSubmit={handleOnSubmit}>
        <label>
          UserName
        </label>
         {/* user name */}
        <input
        type="text"
        name="userName"
        value={state.userName||""}
        onChange={(e)=>dispatch({
          type:"userName",
          nextUserName:e.target.value
        })}
          required
        />
        <br></br>
  {userNameStatus==='no' && <p className="text-danger">user name is not available</p>}
        
        {userNameStatus==='ok' && <p className="text-success">User name is available</p>}
        <br>


        </br>
        {/* email */}
        <label>
          Email
        </label>
        <input
        type="mail"
        name="email"
        value={state.email}
        onChange={(e)=>dispatch({
          type:'email',
          nextEmail:e.target.value
        })}
         required
        />
        <br></br>

        <label>
          LinkedIn Profile Url
        </label>
        {/* linkedin profile url */}
        <input
        type="url"
        name='linkedInProfile'
        value={state.linkedInProfile||""}
        onChange={(e)=>dispatch({
          type:'linkedInProfile',
          nextLinkedIn:e.target.value
        })}
        required
        />
        <br></br>

        {/* github profile url */}
        <label>Git hub Profile</label>
        <input
        type="url"
        name="gitHubProfile"

        value={state.gitHubProfile||""}
        onChange={(e)=>dispatch({
          type:'gitHubProfile',
          nextGitHub:e.target.value
        })}
        required
        />
        <br></br>

        {/* password */}
        <label>Password</label>
        <input
        type="password"
        name="password"
        value={state.password||""}
        onChange={(e)=>dispatch({
          type:'password',
          nextPassword:e.target.value
        })}
         required
        />
        <br></br>

        {/* confirm password  */}

        <label>
          Confirm Password 
        </label>
        <input
        type="password"
        name="confirmPassword"
        value={state.confirmPassword||""}
        onChange={(e)=>dispatch({
          type:'confirmPassword',
          nextConfirmPassword:e.target.value
        })}
         required         
        />
    {formSubmissioon&& <p>User name Already taken </p>}
     <input type="submit" value="Submit"/>


      </form>

      {userStatus==="ok" &&<RegistrationSuccess/>}
      {userStatus==="no" &&<RegistrationFail/>}

      {password[0]&& <p>{password[1]}</p>}
    </div>
  )
};

function passwordValidation(password){
  if(password.length<8 )return [false,"password is weak"];
  if(password.length>25)return [false,"password length is exceeding!"];
  
  // check the criteria
  let result_1=password.match('[a-z]');
  let result_2=password.match('[A-Z]');
  let result_3=password.match(/\d/g);
  let result_4=password.match(/[~!@#$%^&*]/g);
  return [result_1!==null && result_2!==null && result_3!==null && result_4!==null,"please check the password criteria !"];


}

function passwordConfirmPassword(password,confirmPassword){
    return password===confirmPassword;

}