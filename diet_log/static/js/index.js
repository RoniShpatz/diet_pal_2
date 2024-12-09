

// update date to be the current date on top:

const dateOnTop = document.querySelector(".text-muted")
const dateInputs = document.querySelectorAll('input[type="date"]');

function convertDate(dateStr) {
    const parsedDate = new Date(dateStr);
    const year = parsedDate.getFullYear();
    const month = String(parsedDate.getMonth() + 1).padStart(2, '0'); 
    const day = String(parsedDate.getDate()).padStart(2, '0');
  
    // Format the date as YYYY-MM-DD
    return `${year}-${month}-${day}`;
}

dateInputs.forEach(input => {
    input.value = convertDate(dateOnTop.innerText)
})


// water forms - update inputs and show Onclick

const waterTitleForm = document.querySelector('#id_title')
const waterContentForm = document.querySelector(`.water-share p textarea[name="content"]`)

const waterTotal = document.querySelector('#water-total')

const waterFormShareToHide = document.querySelectorAll('.water-share p')
if (waterTitleForm) {
    waterTitleForm.value = 'I drank:'
    if (waterTotal) {
        waterContentForm.value = waterTotal.innerHTML
    }
    
    
    waterFormShareToHide.forEach(p => {
        p.style.display =  "none"
    })
}

const waterForm = document.querySelector('#water-form')

var isOn = false
if (waterForm) {
 waterForm.style.display = "none"
}

if (waterTotal) {
    waterTotal.addEventListener("click", () => {
        if (!isOn) {
            waterForm.style.display = "none"
            isOn = true
        } else {
            waterForm.style.display = "block"
            isOn = false
        }
    })
}


// weight forms - update inputs and show Onclick

const weightInfo = document.querySelector("#weight-info")
const wiehtInput = document.querySelector('.weight-update div p input[name="amount"]')

const wieghtTitleShare = document.querySelector('#wieght-share p input[name="title"]')
const wieghtContentShare = document.querySelector('#wieght-share p textarea[name="content"]')

const weightFormShareHide = document.querySelectorAll('.share-weight p')

if (weightInfo) {
    wiehtInput.value = weightInfo.innerText.match(/\d+/)[0]; 
}


const weightUpdateForm = document.querySelector(".weight-update")
var isWeightOn = false

if (weightUpdateForm) {
    weightUpdateForm.style.display = "none"

    if (weightInfo) {
        weightInfo.addEventListener("click" , () => {
            if (!isWeightOn) {
                weightUpdateForm.style.display = "block"
                isWeightOn = true
            } else {
                weightUpdateForm.style.display = "none"
                isWeightOn = false
            }
        })
    }
}


if (wieghtTitleShare) {
    wieghtTitleShare.value = "I wieght:"
    wieghtContentShare.value = weightInfo.innerText
    
    weightFormShareHide.forEach(p => {
        p.style.display = "none"
    })
}


// workout forms - update inputs and show Onclick

const workoutInfoDou = document.querySelector("#workout-info .workout-dou")
const workoutInfoNum = document.querySelector("#workout-info .workout-name")


const workoutShareName = document.querySelector('#id_name');
if (workoutInfoNum) {
    workoutShareName.value = workoutInfoNum.innerText
}

const workoutShareContent = document.querySelector('#id_duration')
if (workoutInfoDou) {
    workoutShareContent.value =  parseInt(workoutInfoDou.innerText)
}

const workoutUpdsteForm = document.querySelector('.workout-update')
let workoutIsOn = false
if (workoutUpdsteForm) {
    workoutUpdsteForm.style.display = "none"
    const workoutInfo = document.querySelector("#workout-info")
    
    workoutInfo.addEventListener("click", () => {
        if (!workoutIsOn) {
            workoutUpdsteForm.style.display = "none"
            workoutIsOn = true
        } else {
            workoutUpdsteForm.style.display = "block"
            workoutIsOn = false
        }
    }) 
    
}

const wieghtShareForm = document.querySelectorAll('.share-workout p')
const wieghtShareFormTitle = document.querySelector('.share-workout p input[name="title"]')
const wieghtShareFormContent = document.querySelector('.share-workout p textarea[name="content"]')

if (wieghtShareFormTitle) {
    wieghtShareFormTitle.value = 'Workout:'
    wieghtShareFormContent.value = `I workouted for ${workoutInfoDou.innerText} min in ${workoutInfoNum.innerText}`
    
    wieghtShareForm.forEach(p => {
        p.style.display = "none"
    })
}


// Mills forms - update inputs and show Onclick

const mealsUpdateForm = document.querySelectorAll(".meal-update")
const mealTime = document.querySelectorAll(".meal-time")
const mealContent = document.querySelectorAll(".meal-content")

const mealContentInput = document.querySelectorAll(".meal-update p textarea")

if (mealContent.length > 0) {
    for (i=0; i < mealContent.length; i++) {
        mealContentInput[i].value = mealContent[i].innerText
    }
}

function convertToTimeInput(timeString) {
    if (typeof timeString !== 'string') {
        console.error('Invalid input: Not a string', timeString);
        return null;
    }
    timeString = timeString.trim().toLowerCase();
    const timeParts = timeString.match(/(\d{1,2}):(\d{2})\s*(a\.?m\.?|p\.?m\.?)/);
    
    if (!timeParts) {
        console.error('Invalid time format', timeString);
        return null;
    }

    let hours = parseInt(timeParts[1], 10);
    const minutes = parseInt(timeParts[2], 10); 
    const meridian = timeParts[3]; 
    if (minutes > 59) {
        console.error('Invalid minutes', minutes);
        return null;
    }

    if (meridian.includes('p') && hours < 12) {
        hours += 12;
    } else if (meridian.includes('a') && hours === 12) {
        hours = 0;
    }

    const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}`;
    return formattedTime;
}

const mealTimeInput = document.querySelectorAll('.meal-update p input[type="time"]')

if (mealTimeInput.length > 0) {
    for (i=0; i < mealTimeInput.length; i++) {
        mealTimeInput[i].value = convertToTimeInput(mealTime[i].innerText)
    }
}

mealsUpdateForm.forEach(form => {
    form.style.display = "none"
})

const mealHeadLine = document.querySelectorAll(".meal")
const isMealFormOn = false

mealHeadLine.forEach((h5, index) => {
    h5.addEventListener("click", () => {
    // h5.style.cursor = "pointer"
        if (mealsUpdateForm[index].style.display === "block") {
            mealsUpdateForm[index].style.display = "none";
        } else {
            mealsUpdateForm[index].style.display = "block";
        }
    });
});

const titleInputMealShare = document.querySelectorAll('.share-meal p input[name="title"]')
const contentInputMealShare = document.querySelectorAll('.share-meal p textarea[name="content"]')

titleInputMealShare.forEach(title => {
    title.value = "Meal:"
})

contentInputMealShare.forEach((content, index )=> {
    content.value = `At ${mealTime[index].innerText} I ate ${mealContent[index].innerText}`
})

const formMealShare = document.querySelectorAll(".share-meal p")

formMealShare.forEach(form => {
    form.style.display = "none"
})

// add the content of meal in submit meal

const contentSubmitMeal = document.querySelector('.meals_form p textarea[name="content"]')

const selectMealFav = document.querySelector("#fav-meal")

selectMealFav.addEventListener("change", () => {
    const selectedOption = selectMealFav.options[selectMealFav.selectedIndex];
    contentSubmitMeal.value = selectedOption.dataset.content || '';
});