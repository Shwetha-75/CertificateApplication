import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainComponent from "./MainComponent/Main";
import Review from "./ReviewComponent/Main";
import SendMail from "./SendMailComponent/Main";
import Profile from "./ComponentProfile/Profile";
import LandingPage from "./LandingComponent/LandingPage";


export const LoginAdminStatus=React.createContext(null);

function App() {
  
  const [userStatus,setUserStatus]=React.useState(JSON.parse(localStorage.getItem("userStatus"))||false);


  return (
    <LoginAdminStatus.Provider value={{userStatus,setUserStatus}}>
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage/>}></Route>
          <Route path="/profile" element={<MainComponent/>}></Route>
          <Route path="/review" element={<Review/>}></Route>
          <Route path="/mail" element={<SendMail/>}></Route>
          <Route path="/profile" element={<Profile/>} ></Route>
        </Routes>
      </Router>
    </LoginAdminStatus.Provider>
  );
}

export default App;
