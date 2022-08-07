# Python image
FROM debian
#
# Linux utils
RUN \
  apt update &&\
  apt install -y python3 \
  python3-pip \
  tmux &&\
#  
# pip update
  pip install --upgrade pip &&\
  pip install streamlit &&\
# Container init commands
  printf '#! /bin/bash\n/bin/bash\n' > /etc/rc3.d/container_init.sh
#
CMD ["/bin/bash", "/etc/rc3.d/container_init.sh"]