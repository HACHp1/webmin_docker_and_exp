FROM ubuntu
MAINTAINER HACHp1 <hach chp@gmail>

RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.ustc.edu.cn/g" /etc/apt/sources.list
RUN apt-get -y update

RUN echo root:pass | chpasswd
COPY    webmin_1.890_all.deb ./

RUN	apt-get install -y  perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-runtime libio-pty-perl  python	&&\ 
	apt-get  purge  -y  apt-show-versions

RUN	rm /etc/apt/apt.conf.d/docker-gzip-indexes &&\
	apt-get  -y purge apt-show-versions && \
	rm /var/lib/apt/lists/*lz4 && \
	apt-get -o  Acquire::GzipIndexes=false update
RUN	apt-get install -y apt-show-versions &&\
	dpkg  -i webmin_1.890_all.deb

ENV LC_ALL C.UTF-8

EXPOSE 10000

VOLUME ["/etc/webmin"]

CMD /usr/bin/touch /var/webmin/miniserv.log && /usr/sbin/service webmin restart && /usr/bin/tail -f /var/webmin/miniserv.log
