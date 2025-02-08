FROM python:3.10

# Устанавливаем OpenJDK
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем переменную окружения JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Убедимся, что Java установлена
RUN java -version

# Устанавливаем Allure CLI
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.1/allure-commandline-2.23.1.tgz && \
    tar -xvzf allure-commandline-2.23.1.tgz && \
    rm allure-commandline-2.23.1.tgz && \
    mv allure-2.23.1 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure

# Устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install playwright && \
    playwright install && \
    playwright install-deps

# Копируем код проекта в контейнер
COPY . /app
WORKDIR /app

# Команда для запуска тестов с Allure
CMD ["sh", "-c", "pytest -v -s --alluredir=report test_main_page/ && allure serve report"]