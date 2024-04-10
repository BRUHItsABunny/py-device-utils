FROM python:3.11
WORKDIR /tmp

# Set env variables, stabilize versions of each compiler component
RUN echo "${PATH}"
ENV PROTOBUF_VERSION="22.1"
ENV PROTOC_ZIP="protoc-${PROTOBUF_VERSION}-linux-x86_64.zip"
ENV PROTOC_URL="https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/${PROTOC_ZIP}"
# "https://github.com/protocolbuffers/protobuf/releases/download/v3.20.0-rc1/protoc-3.20.0-rc-1-linux-x86_64.zip"

# Download dependencies
RUN apt-get update && apt-get install -y curl git unzip

# Install protobuf (with our version constraint for stability)
RUN echo "Downloading protobuf compiler from: ${PROTOC_URL}"
RUN wget "${PROTOC_URL}"
RUN unzip "${PROTOC_ZIP}" -d ./protoc_dir
RUN chmod 755 -R ./protoc_dir/bin && chmod +x -R ./protoc_dir/bin
RUN cd protoc_dir/bin && ls -R && ./protoc --version
ENV BASE="/usr/local"
RUN cp ./protoc_dir/bin/protoc "${BASE}/bin/"
RUN cp -R ./protoc_dir/include/* "${BASE}/include/"
RUN rm -r ./protoc_dir
RUN ls -R "${BASE}/bin/"
RUN rm "${PROTOC_ZIP}"
# Check protobuf is installed
RUN protoc --version

# Setup Python environment
WORKDIR /proto
RUN pip install protobuf==4.21.8 mypy-protobuf==3.4.0 types-protobuf==4.22.0.2
RUN pip install git+https://github.com/ii64/python-betterproto.git#egg=betterproto
RUN pip install black isort jinja2
ENV PATH="/usr/local/bin:${PATH}"
RUN chmod +x /usr/local/bin/protoc-gen-python_betterproto
RUN which protoc-gen-python_betterproto
RUN protoc-gen-python_betterproto --version

# Copy our repo
COPY . ./

# Setup general includes
ENV PROTO_INC "-I ./ \
  -I ../ \
  -I ../../"

ENV PROTOC_CMD "protoc ${PROTO_INC} --python_betterproto_opt=pydantic_dataclasses,useOptionals=all --python_betterproto_out=. ./*.proto"

# Generate
RUN ls -R /proto
RUN cd /proto/proto-device-utils/ && ${PROTOC_CMD}
RUN ls -R /proto

CMD ["/bin/sh", "-c", "echo Docker done"]