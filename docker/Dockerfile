ARG PYTHON_VERSION=3.7
FROM lambci/lambda:build-python${PYTHON_VERSION}
WORKDIR /var/task

COPY certs /var/task
RUN NOW=$(date '+%Y.%m.%d-%s') && \
  echo "******** Creating Layer for thehive4py ********" && \
  pip install --no-cache-dir -t python \
  thehive4py libmagic && \
  rm -rf python/typing* python/certifi* && \
  zip -r "thehive_$NOW.zip" python && \
  rm -rf python && \
  echo "******** Creating Layer for cortex4py ********" && \
  pip install --no-cache-dir -t python \
  cortex4py libmagic && \
  rm -rf python/typing* python/certifi* && \
  zip -r "cortex_$NOW.zip" python && \
  rm -rf python && \
  echo "******** Creating Layer for certifi ********" && \
  pip install --no-cache-dir -t python \
  certifi && \
  rm -rf python/typing* && \
  cat cacert.pem >> python/certifi/cacert.pem && \
  zip -r "certifi_$NOW.zip" python && \ 
  rm -rf python && \
  echo "******** Layer builds complete ********"

VOLUME ["/app"]