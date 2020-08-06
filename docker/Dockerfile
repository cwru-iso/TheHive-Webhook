ARG PYTHON_VERSION=3.7
FROM lambci/lambda:build-python${PYTHON_VERSION}
WORKDIR /var/task

COPY certs /var/task
RUN NOW=$(date '+%Y.%m.%d-%s') && \
  echo "******** Creating Layer for thehive4py ********" && \
  pip install --no-cache-dir -t python \
  thehive4py libmagic && \
  rm -rf python/typing* && \
  zip -r "thehive_$NOW.zip" python && \
  rm -rf python && \
  echo "******** Creating Layer for cortex4py ********" && \
  pip install --no-cache-dir -t python \
  cortex4py libmagic && \
  rm -rf python/typing* && \
  zip -r "cortex_$NOW.zip" python && \
  rm -rf python && \
  echo "******** Layer builds complete ********"

VOLUME ["/app"]