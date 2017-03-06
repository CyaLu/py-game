FROM index.tenxcloud.com/tenxcloud/centos
MAINTAINER Cya.Lu
RUN yum install -y pcre-devel wget net-tools zlib zlib-devel openssl-devel nginx
EXPOSE 80
