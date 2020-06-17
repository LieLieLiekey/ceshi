#alias rm='rm -i'
#alias cp='cp -i'
#alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
export PATH="$PATH:$HOME/.ft"
export LANG="zh_CN.UTF-8"
export GOPATH=/root/go1.4
#go
export PATH=$PATH:${GOPATH}/bin

export LD_LIBRARY_PATH=/usr/local/lib
export GPG_TTY=/dev/pts/0

#redis
export PATH=$PATH:/usr/local/redis-6.0.5/src

#zookeeper
export PATH=$PATH:/usr/local/apache-zookeeper-3.6.1-bin/bin

#mongdb
export PATH=$PATH:/usr/local/mongodb-4.2.8/bin
