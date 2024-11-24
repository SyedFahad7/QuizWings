module.exports = {
  content: [
    './templates/index.html',
    './templates//.{html,js}', // Adjust paths to your project
  ],
  theme: {
    extend: {
      fontFamily: {
        custom: ['MyCustomFont', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
