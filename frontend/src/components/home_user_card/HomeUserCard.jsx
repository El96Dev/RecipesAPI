import style from "./HomeUserCard.module.css"

export default function HomeUserCard(props) {
    return (
        <div className={style.user_wrapper}>
            <div className={style.user_main_info}>
                <img src={props.image} alt="" className={style.user_avatar}/>
                <h2 className={style.user_username}>{props.nickname}</h2>
            </div>
            <div className={style.user_statistic_info}>
                <div className={style.user_statistic_element}>
                    <h3 className={style.user_statistic_title}>Создано рецептов:</h3>
                    <span className={style.user_statistic_value}>{props.created_recipes}</span>
                </div>
                <div className={style.user_statistic_element}>
                    <h3 className={style.user_statistic_title}>Подписчики:</h3>
                    <span className={style.user_statistic_value}>{props.subscribers}</span>
                </div>
            </div>
        </div>
    )
}