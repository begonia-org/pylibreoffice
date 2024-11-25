#!/bin/bash

# 检查 libmergedlo.so 是否已存在
check_libmergedlo() {
  local paths=(
    "/opt/libreoffice24.8/program"
    "/opt/libreoffice/program"
    "/usr/lib/libreoffice/program"
    "/usr/lib64/libreoffice/program"
  )

  # 在系统库中检查
  if ldconfig -p | grep -q "libmergedlo.so"; then
    echo "libmergedlo.so already found in system libraries."
    return 0
  fi

  # 在指定路径中检查
  for path in "${paths[@]}"; do
    if [[ -f "$path/libmergedlo.so" ]]; then
      echo "libmergedlo.so found in $path."
      return 0
    fi
  done

  # 未找到
  echo "libmergedlo.so not found."
  return 1
}
# 安装cmake
install_cmake() {
    
  wget -O /tmp/cmake-3.22.6-linux-x86_64.tar.gz https://cmake.org/files//v3.22/cmake-3.22.6-linux-x86_64.tar.gz && \
    tar -xvf /tmp/cmake-3.22.6-linux-x86_64.tar.gz -C /usr/local --strip-components=1 && \
    rm -f /tmp/cmake-3.22.6-linux-x86_64.tar.gz && \
    cmake --version
}
# 安装依赖
install_dependencies_rpm() {
  echo "Installing dependencies for RPM-based system (e.g., CentOS/RHEL)..."
  yum install -y libffi-devel zlib-devel \
    fontconfig \
    tar \
    rpm \
    wget \
    && yum clean all && gcc -v
}

install_dependencies_apt() {
  echo "Installing dependencies for APT-based system (e.g., Ubuntu/Debian)..."
  apt-get update && apt-get install -y \
    libffi-dev zlib1g-dev \
    fontconfig \
    tar \
    rpm \
    wget \
    xfonts-base \
    xfonts-75dpi \
    libc6-dev \
    locales \
    libtool \
    && apt-get clean

  # 配置语言环境
  locale-gen zh_CN.UTF-8 && update-locale LANG=zh_CN.UTF-8
}

# 安装 LibreOffice
install_libreoffice_rpm() {
  echo "Installing LibreOffice for RPM-based system..."
  if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz ]]; then
    cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz /tmp/
  else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/rpm/x86_64/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz
  fi
  if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm_langpack_zh-CN.tar.gz ]]; then
    cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm_langpack_zh-CN.tar.gz /tmp/
  else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm_langpack_zh-CN.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/rpm/x86_64/LibreOffice_24.8.3_Linux_x86-64_rpm_langpack_zh-CN.tar.gz
  fi
if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm.tar.gz ]]; then
        cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm.tar.gz /tmp/
else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/rpm/x86_64/LibreOffice_24.8.3_Linux_x86-64_rpm.tar.gz
fi
  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_rpm \
    && yum install -y RPMS/*.rpm

  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm_langpack_zh-CN.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_rpm_langpack_zh-CN/RPMS \
    && yum install -y *.rpm

  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_rpm_sdk/RPMS \
    && yum install -y *.rpm

  yum clean all
  rm -rf /tmp/LibreOffice_24*
}

install_libreoffice_apt() {
  echo "Installing LibreOffice for APT-based system..."
    if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_rpm_sdk.tar.gz ]]; then
    cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_deb_sdk.tar.gz /tmp/
  else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_deb_sdk.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/deb/x86_64/LibreOffice_24.8.3_Linux_x86-64_deb_sdk.tar.gz
  fi
  if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_deb_langpack_zh-CN.tar.gz ]]; then
    cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_deb_langpack_zh-CN.tar.gz /tmp/
  else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_deb_langpack_zh-CN.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/deb/x86_64/LibreOffice_24.8.3_Linux_x86-64_deb_langpack_zh-CN.tar.gz
  fi
if [[ -f thrid_party/LibreOffice_24.8.3_Linux_x86-64_deb.tar.gz ]]; then
        cp thrid_party/LibreOffice_24.8.3_Linux_x86-64_deb.tar.gz /tmp/
else
    wget -O /tmp/LibreOffice_24.8.3_Linux_x86-64_deb.tar.gz \
      https://mirror-hk.koddos.net/tdf/libreoffice/stable/24.8.3/deb/x86_64/LibreOffice_24.8.3_Linux_x86-64_deb.tar.gz
fi

  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_deb.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_deb/DEBS \
    && dpkg -i *.deb

  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_deb_langpack_zh-CN.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_deb_langpack_zh-CN/DEBS \
    && dpkg -i *.deb

  tar -xzf /tmp/LibreOffice_24.8.3_Linux_x86-64_deb_sdk.tar.gz -C /tmp/ \
    && cd /tmp/LibreOffice_24.8.3.2_Linux_x86-64_deb_sdk/DEBS \
    && dpkg -i *.deb

  apt-get clean
  rm -rf /tmp/LibreOffice_24*
}

# 主逻辑
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  if check_libmergedlo; then
    echo "libmergedlo.so already installed. Skipping LibreOffice installation."
    exit 0
  fi

  if [[ -f /etc/redhat-release ]]; then
    install_dependencies_rpm
    install_libreoffice_rpm
  elif [[ -f /etc/debian_version ]]; then
    install_dependencies_apt
    install_libreoffice_apt

  else
    echo "Unsupported Linux distribution."
    exit 1
  fi
elif [[ "$OSTYPE" == "linux-musl" ]]; then
    if grep -q "ID=alpine" /etc/os-release; then
        echo "This is an Alpine Linux system."
        # 在这里添加 Alpine 的具体逻辑
        apk update && \
        apk add --no-cache \
            libffi-dev \
            zlib-dev \
            fontconfig \
            tar \
            wget \
            libreoffice \
            libreofficekit \
            libtool \
            ttf-dejavu \
            font-noto \
            font-noto-cjk
        ls /usr/lib/libreoffice/program/
    else
        echo "This is a musl-based Linux system, but not Alpine."
        # 其他 musl 系统的处理逻辑
    fi
else
  echo "Unknown platform: $OSTYPE"
  exit 1
fi
