import "./style.css"

export default function HomeUsersGrid(props) {
    return (
        <div className="main__users_grid">
            {props.children}
        </div>
    )
}