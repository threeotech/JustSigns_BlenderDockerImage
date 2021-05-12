FROM nytimes/blender:2.92-cpu-ubuntu18.04

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y  --no-install-recommends msodbcsql17 \
    unixodbc-dev \
    unixodbc \
    libpq-dev

WORKDIR /workspace

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN blender --background --python install_addon.py