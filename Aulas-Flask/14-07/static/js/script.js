const registrationForm = document.getElementById('registrationForm');

const emailInput = document.getElementById('email');
const emailError = document.getElementById('emailError');

const usernameInput = document.getElementById('username');
const usernameError = document.getElementById('usernameError');

const passwordInput = document.getElementById('password');
const passwordError = document.getElementById('passwordError');


const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

registrationForm.addEventListener ('submit', function(event) {
    event.preventDefault()

    emailError.textContent = '';

    let isValid = true;

    let blankCounter = 0

    if (emailInput.value.trim() === '') {
        emailError.textContent = 'Por favor, digite seu e-mail.';
        isValid = false;
        ++blankCounter
    } else if (!emailRegex.test(emailInput.value.trim())) {
        emailError.textContent = 'Por favor, digite um e-mail válido.';
        isValid = false;
    }

    if (usernameInput.value.trim() === '') {
        usernameError.textContent = 'Por favor, digite seu nome de usuário.';
        ++blankCounter
        isValid = false;
    }

    if (passwordInput.value.trim() === '') {
        passwordError.textContent = 'Por favor, digite sua senha.';
        ++blankCounter
        isValid = false;
    }
    if (blankCounter === 3) {
        document.getElementById('aviso').textContent = 'Todos os campos são obrigatórios!'
    }
    if (isValid) {
        registrationForm.submit()
    }
})