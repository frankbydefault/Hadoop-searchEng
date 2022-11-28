FROM alpine:latest

RUN apk add --no-cache openjdk8-jre && \
    apk add --no-cache bash && \
    apk add --no-cache python3 && \
    apk add --no-cache openssh && \
    apk add --no-cache sudo && \
    apk add --no-cache openrc

RUN adduser \
    --home "/home/hduser" \
    -D \
    hduser; \
    echo "hduser:supergroup" | \
    chpasswd && \
    adduser hduser wheel && \
    echo "hduser     ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    cd /usr/bin/ && \
    sudo ln -s python3 python

COPY ssh_config /etc/ssh/ssh_config

WORKDIR /home/hduser
USER hduser
RUN ssh-keygen -t rsa -P '' -f $HOME/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && chmod 0600 ~/.ssh/authorized_keys

ENV HADOOP_VERSION=3.3.3
ENV HADOOP_HOME /home/hduser/hadoop-${HADOOP_VERSION}

RUN wget "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
RUN tar -x -C /home/hduser/ -f "hadoop-$HADOOP_VERSION.tar.gz"&& \
    rm -rf ${HADOOP_HOME}/share/doc

ENV HDFS_NAMENODE_USER hduser
ENV HDFS_DATANODE_USER hduser
ENV HDFS_SECONDARYNAMENODE_USER hduser

ENV YARN_RESOURCEMANAGER_USER hduser
ENV YARN_NODEMANAGER_USER hduser

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
COPY core-site.xml $HADOOP_HOME/etc/hadoop/
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/

COPY docker-entrypoint.sh $HADOOP_HOME/etc/hadoop/
RUN sudo chmod +x $HADOOP_HOME/etc/hadoop/docker-entrypoint.sh

ENV PATH $PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ADD wiki/ wiki/

EXPOSE 50070 50075 50010 50020 50090 8020 9000 9864 9870 10020 19888 8088 8030 8031 8032 8033 8040 8042 22

WORKDIR /usr/local/bin
RUN sudo ln -s ${HADOOP_HOME}/etc/hadoop/docker-entrypoint.sh .
WORKDIR /home/hduser

# YARNSTART=0 will prevent yarn scheduler from being launched
ENV YARNSTART 0

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]