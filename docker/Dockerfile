FROM lambci/lambda:build-python3.7
WORKDIR /var/task

RUN pip install --no-cache-dir -t python \
  thehive4py \
  libmagic && \
  rm -rf python/typing* python/certifi* && \
  zip -r thehive_$(date '+%Y.%m.%d-%s').zip python && \
  rm -rf python

RUN pip install --no-cache-dir -t python \
  cortex4py \
  libmagic && \
  rm -rf python/typing* python/certifi* && \
  zip -r cortex_$(date '+%Y.%m.%d-%s').zip python && \
  rm -rf python

COPY certs /var/task
RUN pip install --no-cache-dir -t python certifi && \
  rm -rf python/typing* && \
  cat cacert.pam >> python/certifi/cacert.pem && \
  zip -r certifi_$(date '+%Y.%m.%d-%s').zip python && \ 
  rm -rf python

VOLUME ["/app"]