FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# Install packages
RUN conda install --yes \
    numpy==1.17.3 \
    Keras==2.2.4 \
    Pillow==6.2.1

# Install Java
RUN apt-get -f install && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy files over
# Copy over konduit.jar and dependencies
COPY mnist /tmp/mnist

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

EXPOSE 65322

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]