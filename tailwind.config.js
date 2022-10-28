/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: ["./templates/**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                'nice': '#1E313B'
            },
        },
    },
    plugins: [],
}
