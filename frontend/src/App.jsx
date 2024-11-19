import "./styles/main.css"
import "./styles/header.css"
import "./styles/footer.css"

import Navbar from "./components/navbar/Navbar"
import Mainlogo from "./components/mainlogo/Mainlogo"
import Header from "./components/header/Header"
import Main from "./components/main/Main"

import pasta from "./img/pasta.jpg"
import avatar from "./img/ava.png"

import {users, recipes_filters, users_filters} from "../data"

import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import axios from "axios"
import { useEffect } from "react"
import { useState } from 'react'
import HomeRecipyGrid from "./components/home_recipy_grid/HomeRecipyGrid"
import RecipyCard from "./components/recipy_card/RecipyCard"
import Footer from "./components/footer/Footer"
import HeaderProfileRef from "./components/header_profile_ref/HeaderProfileRef"
import HomeUsersGrid from "./components/home_users_grid/HomeUsersGrid"
import HomeUserCard from "./components/home_user_card/HomeUserCard"
import HomeFilters from "./components/home_filters/HomeFilters"
import Select from "./components/select/Select"
import HomeRecipes from "./pages/HomeRecipes"
import HomeUsers from "./pages/HomeUsers"
import HomeArticles from "./pages/HomeArticles"
import HomeRecipy from "./pages/HomeRecipy"
import HomeArticle from "./pages/HomeArticle"


function App() {
  
  return (
    <div className="App">
      <HomeRecipes/>
      <Router>
        <Routes>
          <Route path="/" element={<HomeRecipes/>}/>
          <Route path="/users" element={<HomeUsers/>}/>
          <Route path="/articles" element={<HomeArticles/>}/>
          <Route path="/articles/:id" element={<HomeArticle/>}/>
          <Route path="/recipes/:id" element={<HomeRecipy/>}/>
        </Routes>
      </Router>
    </div>
  )
}

export default App
