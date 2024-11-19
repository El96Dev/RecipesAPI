import {useParams} from "react-router-dom" 
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
import Recipy from "../components/recipy/Recipy"

import {recipes_filters, recipes} from "../../data"


export default function HomeRecipy() {

    const {id} = useParams();

    return (
        <>
            <Header>
                <Mainlogo></Mainlogo>
                <Navbar></Navbar>
                <HeaderProfileRef></HeaderProfileRef>
            </Header>
            <Main>

                <p>{id}</p>
                <Recipy {...recipes[0]}/>
        
            </Main>
    
            <Footer></Footer>
        </>
    )
}