import "./style.css"

export default function Select(props) {
    return (
        <div className="filters__element">
            <div className="filters__label">{props.title}</div>
            <select>
                {props.values.map((value) => {
                    return <option>{value}</option>
                })}
            </select>
        </div>
    )
}