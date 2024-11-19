import "./style.css"
import Mainlogo from "../mainlogo/Mainlogo"
import Navbar from "../navbar/Navbar"


export default function Header(props) {
    return (
        <header className="header">
            {props.children}
        </header>
    )
}