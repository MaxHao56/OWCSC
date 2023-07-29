import React from "react";
import {Routes,Route} from 'react-router-dom'
import Home from "./pages/homepage/Home";
import Survey from "./pages/surveys/Survey";


function App() {
  return (
   
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/survey" element={<Survey/>}/>
    </Routes>
 
  );
}

export default App;
