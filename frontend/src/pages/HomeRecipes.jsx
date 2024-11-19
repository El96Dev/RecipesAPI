import { NavLink } from "react-router-dom"
import Header from "../components/header/Header"
import Mainlogo from "../components/mainlogo/Mainlogo"
import Navbar from "../components/navbar/Navbar"
import HeaderProfileRef from "../components/header_profile_ref/HeaderProfileRef"
import Main from "../components/main/Main"
import HomeFilters from "../components/home_filters/HomeFilters"
import HomeRecipyGrid from "../components/home_recipy_grid/HomeRecipyGrid"
import RecipyCard from "../components/recipy_card/RecipyCard"
import Select from "../components/select/Select"
import Footer from "../components/footer/Footer"

import {recipes_filters, recipes} from "../../data"


export default function HomeRecipes() {
    return (
        <>
            <Header>
                <Mainlogo></Mainlogo>
                <Navbar></Navbar>
                <HeaderProfileRef></HeaderProfileRef>
            </Header>
            <Main>
        
                <HomeFilters>
                    <Select title="Кухня" values={cuisines}/>
                    <Select title="Категория" values={categories}/>
                </HomeFilters>

                <HomeRecipyGrid>
                    { recipes.map((recipy) => {
                        return <NavLink to="/recipes/1">
                                    <RecipyCard {...recipy}/>
                               </NavLink>
                        
                    })

                    }
                </HomeRecipyGrid>
        
            </Main>
    
            <Footer></Footer>
        </>
    )
}