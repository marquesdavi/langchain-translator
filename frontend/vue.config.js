module.exports = {
  devServer: {
    port: 3000,
    proxy: {
      '/translate': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/translate': '/translate' }
      }
    }
  }
};
