// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Produce from "./pages/Produce";
import Forum from "./pages/Forum";
import Equipment from "./pages/Equipment";
import Login from "./pages/Login";
import Register from "./pages/Register"; // Ensure this line is correct
import Navbar from "./components/Navbar";
import "./App.css";

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/produce" element={<Produce />} />
          <Route path="/forum" element={<Forum />} />
          <Route path="/equipment" element={<Equipment />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} /> {/* Ensure this line is correct */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;