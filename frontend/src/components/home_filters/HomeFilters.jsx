import "./style.css"


export default function HomeFilters(props) {
    return (
        <div className="main__filters">
            <span className="filters__title">Фильтры</span>
            {props.children}
        </div>
    )
}