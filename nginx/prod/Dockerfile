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
COPY nginx/prod/prod.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
