import React from "react";
// import Main from "./Component/Main";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import MainComponent from "./MainComponent/Main";
// import Review from "./ReviewComponent/Main";
// import SendMail from "./SendMailComponent/Main";
// import NavigationBar from "./MainComponent/NavigationBar";
// import Profile from "./ComponentProfile/Profile";
import Registration from "./Registration/Registration";

function App() {

  return (
    <div className="app">
      {/* <Router>
      <NavigationBar/>
        <Routes>
          <Route path="/" element={<Registration  />}></Route>
          <Route path="/review" element={<Review/>}></Route>
          <Route path="/mail" element={<SendMail/>}></Route>
          <Route  path="/profile" element={<Profile/>} ></Route>
        </Routes>
      </Router> */}
      <Registration/>
      {/* <MainComponent/> */}
     {/* <Main/> */}
    </div>
  );
}

export default App;
