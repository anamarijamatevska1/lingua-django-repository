const quizSection = document.getElementById('quizSection')
const quizQuestionSection = document.getElementById('quizQuestionSection')
const trophySection = document.getElementById('trophySection')

const showQuizQuestions = () => {
    quizSection.classList.toggle('d-none')
    quizQuestionSection.classList.toggle('d-none')
}

const openQuiz = (id) => {
    window.location.href = `?id=${id}`
}

const finishQuiz = () => {
    quizQuestionSection.classList.toggle('d-none')
    trophySection.classList.toggle('d-none')
}