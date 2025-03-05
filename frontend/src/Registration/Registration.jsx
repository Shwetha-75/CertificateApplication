import React from 'react'


function reducer(state={
  userName:'',
  email:"",
  linkedIn:'',
  gitHub:"",
  password:"",
  confirmPassword:''
},action){
     switch(action.type){
  
           case "username":return {
            ...state,
            userName:action.nextUserName
           }

           case "email": return {
            ...state,
            email:action.nextEmail
           }

           case "linkedIn":return{
            ...state,
            linkedIn:action.nextLinkedIn
           }

           case "gitHub":return{
            ...state,
            gitHub:action.nextGitHub
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

  const [state,dispatch]=React.useReducer(reducer,{
    userName:'',
    email:"",
    linkedIn:'',
    gitHub:"",
    password:"",
    confirmPassword:''
  })


  const handleOnSubmit=(e)=>{
    console.log(state)
    e.preventDefault();
  }
    


  return (
    <div>
      <form onSubmit={handleOnSubmit}>
        <label>
          UserName
        </label>
         {/* user name */}
        <input
        type="text"
        name="username"
        value={state.userName||""}
        onChange={(e)=>dispatch({
          type:"username",
          nextUserName:e.target.value
        })}
        />
        <br></br>
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
        />
        <br></br>

        <label>
          LinkedIn Profile Url
        </label>
        {/* linkedin profile url */}
        <input
        type="url"
        name='linkedIn'
        value={state.linkedIn||""}
        onChange={(e)=>dispatch({
          type:'linkedIn',
          nextLinkedIn:e.target.value
        })}
        />
        <br></br>

        {/* github profile url */}
        <label>Git hub Profile</label>
        <input
        type="url"
        name="gitHub"

        value={state.gitHub||""}
        onChange={(e)=>dispatch({
          type:'gitHub',
          nextGitHub:e.target.value
        })}
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
        />
     <input type="submit" value="Submit"/>
      </form>
    </div>
  )
}
