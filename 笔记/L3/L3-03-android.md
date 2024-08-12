# InternLM 1.8B 模型 Android 端侧部署实践

## 环境配置
安装rust：
```yaml
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
curl --proto '=https' --tlsv1.2 -sSf https://mirrors.ustc.edu.cn/misc/rustup-install.sh  | sh

```
安装Android Studio:
```yaml
mkdir -p /root/android && cd /root/android
wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/2024.1.1.12/android-studio-2024.1.1.12-linux.tar.gz
tar -xvzf android-studio-2024.1.1.12-linux.tar.gz
cd android-studio
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip?hl=zh-cn
unzip commandlinetools-linux-11076708_latest.zip\?hl\=zh-cn
export JAVA_HOME=/root/Downloads/android-studio/jbr
cmdline-tools/bin/sdkmanager "ndk;27.0.12077973" "cmake;3.22.1"  "platforms;android-34" "build-tools;33.0.1" --sdk_root='sdk'
```

## 转换模型
安装mlc-llm:
conda create --name mlc-prebuilt  python=3.11
conda activate mlc-prebuilt
conda install -c conda-forge git-lfs
pip install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 transformers sentencepiece protobuf
wget https://github.com/mlc-ai/package/releases/download/v0.9.dev0/mlc_llm_nightly_cu122-0.1.dev1445-cp311-cp311-manylinux_2_28_x86_64.whl
wget https://github.com/mlc-ai/package/releases/download/v0.9.dev0/mlc_ai_nightly_cu122-0.15.dev404-cp311-cp311-manylinux_2_28_x86_64.whl
pip install mlc_ai_nightly_cu122-0.15.dev404-cp311-cp311-manylinux_2_28_x86_64.whl
pip install mlc_llm_nightly_cu122-0.1.dev1445-cp311-cp311-manylinux_2_28_x86_64.whl