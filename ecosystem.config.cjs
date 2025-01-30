module.exports = {
  apps: [
    {
      name: 'cse-lbds-server',
      script: 'venv/bin/uvicorn', // Chỉ rõ đường dẫn đến Uvicorn
      args: 'app.main:app --host 0.0.0.0 --port 8000', // Đảm bảo đúng tên và cổng
      interpreter: 'python3', // Sử dụng interpreter Python
    },
  ],
}
