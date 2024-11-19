import { NavLink } from "react-router-dom"
import { useParams } from "react-router-dom"
import Header from "../components/header/Header"
import Mainlogo from "../components/mainlogo/Mainlogo"
import Navbar from "../components/navbar/Navbar"
import HeaderProfileRef from "../components/header_profile_ref/HeaderProfileRef"
import Main from "../components/main/Main"
import Footer from "../components/footer/Footer"
import Article from "../components/article/Article"

import {articles} from "../../data"


export default function HomeArticles() {

    const {id} = useParams();

    return (
        <>
            <Header>
                <Mainlogo></Mainlogo>
                <Navbar></Navbar>
                <HeaderProfileRef></HeaderProfileRef>
            </Header>
            <Main>

                <Article {...articles[0]}/>
        
            </Main>
    
            <Footer></Footer>
        </>
    )
}