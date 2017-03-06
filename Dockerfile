FROM index.tenxcloud.com/tenxcloud/centos
MAINTAINER Cya.Lu
RUN yum install -y pcre-devel wget net-tools gcc zlib zlib-devel make openssl-devel
ADD http://nginx.org/download/nginx-1.8.0.tar.gz
RUN tar zxvf nginx-1.8.0.tar.gz .
RUN mkdir -p /usr/local/nginx
RUN cd nginx-1.8.0 && ./configure --prefix=/usr/local/nginx && make && make install
EXPOSE 80
