const root = document.documentElement
const themeToggler = document.getElementById('theme-toggler')
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)')

// 1. Set theme by user's choice in localStorage
const theme = localStorage.getItem('theme')
if (theme == 'dark') {
  setDarkTheme()
} else if (theme == 'light') {
  setLightTheme()
} else {
  // 2. Set theme by system default
  prefersDarkScheme.matches ? setDarkTheme() : setLightTheme()
}

// 3. Set theme by user's choice with click event
themeToggler.addEventListener('click', function() {
  const isDarkTheme = root.classList.contains('dark-theme')
  if (isDarkTheme) {
    setLightTheme()
    localStorage.setItem('theme', 'light')
  } else {
    setDarkTheme()
    localStorage.setItem('theme', 'dark')
  }
})

function setDarkTheme() {
  if (root.className !== 'dark-theme') {
    root.className = 'dark-theme'
  }
  themeToggler.innerHTML = `
  <img src="./_static/dark-theme.png"></img>
  Dark Theme
  `
}

function setLightTheme() {
  if (root.className === 'dark-theme') {
    root.removeAttribute('class')
  }
  themeToggler.innerHTML =  `
  <img src="./_static/light-theme.png"></img>
  Light Theme
  `
}
