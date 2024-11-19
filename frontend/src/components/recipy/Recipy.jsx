import { NavLink } from "react-router-dom"
import "./style.css"

export default function Recipy(props) {
    return (
        <div className="recipy_wrapper">
            <div className="recipy_inner_wrapper">
                <img src={props.image} alt="" className="recipy_image"/>
                <div className="recipy_meta_wrapper">
                    <h2 className="recipy_title">{props.title}</h2>
                    <div className="recipy_meta_user">
                        <h3 className="recipy_author_title">Автор:</h3>
                        <a href="#" className="recipy_author_ref">{props.author}</a>
                    </div>
                    <div className="recipy_meta_updated">
                        <h3 className="recipy_updated_title">Обновлено:</h3>
                        <span className="recipy_updated_value">{props.last_updated}</span>
                    </div>
                    <div className="main__recipy_likes_wrapper">
                        <NavLink to="/">
                            <svg className="main__recipy_like_svg" fill="#000000" height="18px" width="18px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                            viewBox="0 0 51.997 51.997" xml:space="preserve">
                                <path d="M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905
                                    c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478
                                    c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014
                                    C52.216,18.553,51.97,16.611,51.911,16.242z"/>
                            </svg>
                            <span className="main__recipy_likes_value">{props.likes}</span>
                        </NavLink>
                    </div>
                </div>
                <h3 className="recipy_description_title">Описание</h3>
                <p className="recipy_description_text">{props.description}</p>

                <h3 className="recipy_ingredients_title">Ингредиенты</h3>
                <ul className="recipy_ingredients_list">

                        {props.ingredients.map((ingredient) => {
                            return (
                                <li className="recipy_ingredients_list_element">
                                    <h4 className="recipy_ingredient_title">{ingredient.name}</h4>
                                    <span className="recipy_ingredient_amount">{ingredient.amount}</span>
                                </li>
                            )
                        })}
                </ul>
                <h3 className="recipy_steps_title">Шаги</h3>
                <ul className="recipy_steps_list">

                    {props.steps.map((step) => {
                        return (
                            <li className="recipy_steps_list_element">
                                <h4 className="recipy_step_title">Шаг {step.number}</h4>
                                <p className="recipy_step_text">{step.text}</p>
                            </li>
                        )
                    })}

                </ul>
            </div>
        </div>
    )
}