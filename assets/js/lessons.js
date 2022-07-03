const courseSection = document.getElementById('courseSection')
const lessonsSection = document.getElementById('lessonsSection')

const openCourse = (id) => {
    window.location.href = `?id=${id}`
}

const showCourseLessons = () => {
    courseSection.classList.toggle('d-none')
    lessonsSection.classList.toggle('d-none')
}

