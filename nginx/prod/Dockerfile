# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app/
COPY frontend/package*.json /app/
RUN npm cache verify
RUN npm install
COPY frontend /app/
RUN npm run build

# production stage
FROM nginx:alpine as production-stage
COPY nginx/prod/nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available/
COPY nginx/prod/prod.conf /etc/nginx/sites-available/codingrush.cf.vhost

RUN mkdir /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/codingrush.cf.vhost /etc/nginx/sites-enabled/
RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir /usr/local/sbin/
RUN wget https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/install-ngxblocker -O /usr/local/sbin/install-ngxblocker
RUN chmod +x /usr/local/sbin/install-ngxblocker
RUN /usr/local/sbin/install-ngxblocker -x
RUN chmod +x /usr/local/sbin/setup-ngxblocker
RUN chmod +x /usr/local/sbin/update-ngxblocker
RUN /usr/local/sbin/setup-ngxblocker -x

COPY --from=build-stage /app/dist /dist/
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
