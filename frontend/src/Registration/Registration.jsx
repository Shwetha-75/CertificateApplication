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
            password:action.password
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
  

  return (
    <div>
      <form>
         {/* user name */}
        <input
        type="text"
        name="username"
        value={state.userName}

        onChange={(e)=>dispatch({
          type:"username",
          nextUserName:e.target.value
        })}
        />
        {/* email */}
        <input
        type="mail"
        name="email"
        value={state.email}
        onChange={(e)=>dispatch({
          type:'email',
          nextEmail:e.target.value
        })}

        />
        {/* linkedin profile url */}
        <input
        type="url"
        name='linkedIn'
        value={state.linkedIn}
        onChange={(e)=>dispatch({
          type:'linkedIn',
          nextLinkedIn:e.target.value
        })}
        />
        {/* github profile url */}
        <input
        type="url"
        name="gitHub"

        value={state.gitHub}
        onChange={(e)=>dispatch({
          type:'gitHub',
          nextGitHub:e.target.value
        })}
        />
        {/* password */}
        <input
        type="password"
        name="password"

        />

        {/* confirm password  */}
        <input/>

      </form>
    </div>
  )
}
