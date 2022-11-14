/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: ["./templates/**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                'nice': '#1E313B',
                'schgreen': '#18C187'
            },
        },
    },
    plugins: [],
}
