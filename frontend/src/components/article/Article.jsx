import { NavLink } from "react-router-dom";
import style from "./Article.module.css"


export default function Article(props) {
    return (
        <div className={style.article_wrapper}>

            <div id={style.article_inner_wrapper}>
                <img src={props.image} alt={props.image} className={style.article_image} />
                <h2 className={style.article_title}>{props.title}</h2>
                <p className={style.article_text}>{props.text}</p>
            </div>


        </div>
    )
}