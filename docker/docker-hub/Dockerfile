FROM alpine:3.10.3

RUN apk add --update \
    python3 \
    python3-dev \
    py-pip \
    build-base \
    bash \
  && pip3 install --no-cache-dir --upgrade pip \
  && rm -rf /var/cache/* \
  && rm -rf /root/.cache/*

RUN cd /usr/bin \
  && ln -sf python3 python \
  && ln -sf pip3 pip

# Install Java8
RUN apk add --no-cache openjdk8

# Set environment
ENV JAVA_HOME /opt/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin

WORKDIR /konduit

# Install app dependencies
COPY requirements.txt /konduit
#RUN pip install -r requirements.txt

# Copy over konduit.jar and dependencies
COPY mnist /konduit/mnist

EXPOSE 65322

CMD ["java", "-version"]
#CMD tail -f /dev/null
