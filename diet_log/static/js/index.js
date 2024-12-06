const update_date = document.querySelectorAll('input[type="date"]')
function convertDate(dateStr) {
    if (!dateStr) {
      throw new Error("Invalid date string");
    }
    const date = new Date(dateStr);

    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); 
    const day = String(date.getDate()).padStart(2, '0');
  
    return `${year}-${month}-${day}`;
  }

const inputDate = "{{current_date}}"
const outputDate = convertDate(inputDate)
update_date.forEach(input => {
input.value = outputDate
})
// fill the wieght info in the form
const updateWeight = document.querySelectorAll('.weight-update input[name="amount"]')
const weightNum = document.querySelectorAll('.wieght_num')
for (let i=0; i < weightNum.length; i++){
updateWeight[i].value = weightNum[i].innerText
}
// fill the workout info in the form
const workoutName = document.querySelectorAll(".workout-name")
const workoutDuration= document.querySelectorAll(".workout-duration")
const updateWorkout = document.querySelectorAll('.workout-update input[name="duration"]')
const updateSelectWorkout = document.querySelectorAll('.workout-update select[name="name"]')

for (let i=0; i < updateWorkout.length; i ++) {
updateWorkout[i].value = workoutDuration[i].innerHTML
updateSelectWorkout[i].value = workoutName[i].innerHTML
}
//fill the meals form
const mealContent = document.querySelectorAll(".meal-content")
const mealTime = document.querySelectorAll(".meal-time")

const mealContentInput = document.querySelectorAll('.meal-update textarea[name="content"]')
const mealTimeInput = document.querySelectorAll('.meal-update input[name="time"]')

for (let i=0; i < mealContent.length; i++) {
mealContentInput[i].value = mealContent[i].innerHTML
mealTimeInput[i].value = mealTime[i].innerHTML 
}

// share post form water
const titleInputWater = document.querySelector('.water-share input[name="title"]')
const waterTotal = document.querySelector('#water-total')
const contentInputWater = document.querySelector('.water-share textarea[name="content"]')

titleInputWater.value = `Water on the ${inputDate}`
contentInputWater.value = `I drank ${waterTotal.innerText} today!`

const hidePostWaterShare = document.querySelectorAll('.water-share p')
hidePostWaterShare.forEach(p => {
p.style.display = "none"
})

// share post form weight
const weightFormPost = document.querySelectorAll(".share-weight p")
const weightShareTitle = document.querySelectorAll('.share-weight input[name="title"]')
const weightShareContent = document.querySelectorAll('.share-weight textarea[name="content"]')

weightShareTitle.forEach(title => {
title.value = `Weight on the ${inputDate}`
})
for (let i=0; i < weightNum.length; i++){
weightShareContent[i].value = `I wieght ${weightNum[i].innerText} today!`
}
weightFormPost.forEach(p => {
p.style.display = "none"
})

// share post form workout
const workoutFormPost = document.querySelectorAll(".share-workout p")
const workoutShareTitle = document.querySelectorAll('.share-workout input[name="title"]')
const workoutShareContent = document.querySelectorAll('.share-workout textarea[name="content"]')

workoutShareTitle.forEach(title => {
title.value = `Workout on the ${inputDate}`
})
if (workoutName.length >0) {
for (let i=0; i < weightNum.length; i++){
workoutShareContent[i].value = `I wast ${ workoutName[i].innerText} for ${workoutDuration[i].innerHTML} Min.`
}
workoutFormPost.forEach(p => {
p.style.display = "none"
})
}

// share post form meal

const mealFormPost = document.querySelectorAll(".share-meal p")
const mealShareTitle = document.querySelectorAll('.share-meal input[name="title"]')
const mealShareContent = document.querySelectorAll('.share-meal textarea[name="content"]')

mealShareTitle.forEach(title => {
title.value = `Meal on the ${inputDate}`
})
for (let i=0; i < mealContent.length; i++){
mealShareContent[i].value = `I ate ${ mealContent[i].innerText}.`
}
mealFormPost.forEach(p => {
p.style.display = "none"
})

// add content of favorite meal to content
const option = document.getElementById("fav-meal")
const contentMeal = document.querySelector('.meals_form textarea[name="content"]')

option.addEventListener("change", () => {
  // Get the selected option
  const selectedOption = option.options[option.selectedIndex]; 

  // Get the data-content attribute from the selected option
  const mealContent = selectedOption.getAttribute("data-content");

  // Update the textarea with the meal content
  if (contentMeal) {
    contentMeal.value = mealContent || ""; // Set the content or clear if no value
  }
});


