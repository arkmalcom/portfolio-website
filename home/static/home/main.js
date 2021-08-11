const currentTheme = localStorage.getItem('theme');

if(currentTheme === 'theme-dark') {
    setTheme('theme-dark');
} else {
    setTheme('theme-light');
}

function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.setAttribute("data-theme", themeName);
}
