import axios from "axios";


const cuisines = axios.get("http://127.0.0.1:8000/api/v1/recipes/categories").then(result => {
    setCategories(result.data);
  })


const getCategories = () => {
    axios.get("http://127.0.0.1:8000/api/v1/recipes/categories").then(result => {
      setCategories(result.data);
    })
  }