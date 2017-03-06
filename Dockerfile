FROM index.tenxcloud.com/tenxcloud/centos
MAINTAINER Cya.Lu
RUN yum install -y pcre-devel wget net-tools gcc zlib zlib-devel make openssl-devel nginx
EXPOSE 80
