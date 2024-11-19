import "./style.css"


export default function HomeArticleGrid(props) {
    return (
        <div className="home_article_grid">
            <h2 className="home_articles_title">Статьи</h2>
            {props.children}
        </div>
    )
}