import { NavLink } from "react-router-dom"
import "./style.css"

export default function Navbar() {
    return (
        <nav className="header__nav">
            <NavLink to="/">
                <span>Рецепты</span>
            </NavLink>
            <NavLink to="/users">
                <span>Пользователи</span>
            </NavLink>
            <NavLink to="/articles">
                <span>Статьи</span>
            </NavLink>

        </nav>
    )
}
