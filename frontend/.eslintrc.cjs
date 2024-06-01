/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-prettier/skip-formatting'
  ],
  env: {
    browser: true,
    es2021: true,
    node: true // Add this line to include the Node.js environment
  },
  parserOptions: {
    ecmaVersion: 'latest'
  }
}
