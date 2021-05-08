FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available/
COPY dev.conf /etc/nginx/sites-available/codingrush.cf.vhost

RUN mkdir /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/codingrush.cf.vhost /etc/nginx/sites-enabled/
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
