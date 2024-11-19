import style from "./HomeArticleCard.module.css"


export default function HomeArticleCard(props) {
    return (
        <div className={style.home_article_card}>
            <img src={props.image} alt="ssdf" className={style.article_image} />
            <div className={style.article_preview_wrapper}>
                <h2 className={style.article_title}>{props.title}</h2>
                <p className={style.article_text}>{props.text}</p>
            </div>
        </div>
    )
}