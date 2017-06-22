FROM python2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /data/www/GitHub/blog_project \
    && mkdir -p /var/log/django

WORKDIR /data/www/GitHub/blog_project
ADD requirements.txt /data/www/GitHub/blog_project

RUN pip install -r requirement.txt

ADD . /data/www/GitHub/blog_project
WORKDIR /data/www/GitHub/blog_project/source/projects/blog


