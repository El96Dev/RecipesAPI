import Header from "../components/header/Header"
import Mainlogo from "../components/mainlogo/Mainlogo"
import Navbar from "../components/navbar/Navbar"
import HeaderProfileRef from "../components/header_profile_ref/HeaderProfileRef"
import Main from "../components/main/Main"
import HomeFilters from "../components/home_filters/HomeFilters"
import HomeUsersGrid from "../components/home_users_grid/HomeUsersGrid"
import HomeUserCard from "../components/home_user_card/HomeUserCard"
import Select from "../components/select/Select"
import Footer from "../components/footer/Footer"

import {users_filters, users} from "../../data"


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
                    { users_filters.map((filter) => {
                        return <Select title={filter.title} values={filter.values}/>
                    })}
                </HomeFilters>
                <HomeUsersGrid>
                    {   users.map((user) => {
                            return <HomeUserCard nickname={user.nickname} 
                            subscribers={user.subscribers} image={user.image}/>
                        })
                    }
                </HomeUsersGrid>
                
        
            </Main>
    
            <Footer></Footer>
        </>
    )
}