console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const closeBtn = document.getElementById('close-button')

const url = window.location.href
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk')
    const topic = modalBtn.getAttribute('data-topic')
    const name = modalBtn.getAttribute('data-quizz')
    const noq = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const passing_score = modalBtn.getAttribute('data-passing_score')
    const duration = modalBtn.getAttribute('data-time')


    modalBody.innerHTML = `
        <div class="h6 mb-3">Are you sure you want to start the "<b>${name}</b>" test ?</div>
        <div class="text">
            <ul>
                <li>Topic: <b>${topic}</b></li>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>Number of questions: <b>${noq}</b></li>
                <li>Score to pass: <b>${passing_score}%</b></li>
                <li>Time: <b>${duration} min</b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click',   () => {
        window.location.href = url + pk
    })
}))
