
// fill name amd content in input fileds
const nameMealInput = document.querySelectorAll(".name-meal")
const contentMealInput = document.querySelectorAll(".content-meal")

const inputFavMeal = document.querySelectorAll('.fav-meal-form p input[name="name"]')
const inputFavMealContent = document.querySelectorAll('.fav-meal-form p textarea[name="content"]')

nameMealInput.forEach((name, index) => {
    inputFavMeal[index].value = nameMealInput[index].innerText 
})

contentMealInput.forEach((name, index) => {
    inputFavMealContent[index].value = contentMealInput[index].innerText 
})

const mealForm = document.querySelectorAll(".fav-meal-update")

mealForm.forEach( form => {
    form.style.display = "none"
})

nameMealInput.forEach((name, index) => {
    name.addEventListener("click", () => {
        if (mealForm[index].style.display === "block") {
            mealForm[index].style.display = "none";
        } else {
            mealForm[index].style.display = "block";
        } 
    })
})

