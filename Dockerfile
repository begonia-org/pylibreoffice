FROM python:3.11.10-alpine3.20

LABEL maintainer="vforfreedom96@gmail.com"
ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN.UTF-8
RUN apk update && \
    apk add --no-cache \
    bash \
    curl \
    git \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    cmake \
    make \
    ninja \
    ninja-build \
    libreoffice \
    libreofficekit \
    libtool \
    ttf-dejavu \
    font-noto \
    font-noto-cjk \
    wqy-zenhei \
    supervisor \
    ttf-freefont && \
    apk cache clean && \
    rm -rf /var/cache/apk/* && \
    pip install --upgrade pip
ADD . app/
WORKDIR /app
RUN python3 -m pip install Cython pybind11 scikit-build && \
    python3 setup.py build sdist && \
    python3 -m pip install dist/*.tar.gz && \
    rm -rf dist && \
    rm -rf /root/.cache/pip && \
    rm -rf /root/.cache && \
    cd ../ && \
    cp -r /app/example . && \
    rm -rf /app && \
    python3 example/example.py

CMD ["/bin/bash"]