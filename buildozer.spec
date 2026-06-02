[app]

# ── 应用基本信息
title = 皮肤病变AI分析
package.name = skinlesionai
package.domain = org.skinai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0

# ── 依赖包
requirements = python3,kivy==2.3.0,pillow,plyer

# ── Android 权限
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# ── Android 配置
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.ndk_api = 24
android.accept_sdk_license = True
android.archs = armeabi-v7a

# ── 屏幕方向
orientation = portrait

# ── 全屏
fullscreen = 0

# ── 图标（替换为实际图标路径）
# icon.filename = %(source.dir)s/assets/icon.png
# presplash.filename = %(source.dir)s/assets/splash.png

# ── iOS（不使用）
[buildozer]
log_level = 2
warn_on_root = 0

# 构建目录
build_dir = ./.buildozer
bin_dir = ./bin
