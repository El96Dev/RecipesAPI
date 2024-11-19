import { NavLink } from "react-router-dom"
import Header from "../components/header/Header"
import Mainlogo from "../components/mainlogo/Mainlogo"
import Navbar from "../components/navbar/Navbar"
import HeaderProfileRef from "../components/header_profile_ref/HeaderProfileRef"
import Main from "../components/main/Main"
import HomeFilters from "../components/home_filters/HomeFilters"
import HomeArticleGrid from "../components/home_articles_grid/HomeArticlesGrid"
import HomeArticleCard from "../components/home_article_card/HomeArticleCard"
import Select from "../components/select/Select"
import Footer from "../components/footer/Footer"

import {articles} from "../../data"


export default function HomeArticles() {
    return (
        <>
            <Header>
                <Mainlogo></Mainlogo>
                <Navbar></Navbar>
                <HeaderProfileRef></HeaderProfileRef>
            </Header>
            <Main>

                <HomeArticleGrid>
                    { articles.map((article) => {
                            return <NavLink to="/articles/:id">
                                    <HomeArticleCard title={article.title} text={article.text} image={article.image}/>
                                   </NavLink>
                        })
                    }
                </HomeArticleGrid>
        
            </Main>
    
            <Footer></Footer>
        </>
    )
}