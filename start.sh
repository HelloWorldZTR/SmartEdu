#!/bin/bash

echo "🚀 启动 SmartEdu 组队平台..."

# 检查 Node.js 版本
echo "📋 检查环境..."
node --version
npm --version

# 安装依赖
echo "📦 安装依赖..."
npm install

# 启动开发服务器
echo "🌐 启动开发服务器..."
npm run dev 