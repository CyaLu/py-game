#Comment
FROM index.tenxcloud.com/tenxcloud/centos
RUN echo 'we are running some # of cool things'
MAINTAINER Cya.Lu
RUN yum install -y pcre-devel wget net-tools zlib zlib-devel openssl-devel nginx
EXPOSE 80
