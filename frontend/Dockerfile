FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app/

COPY package*.json ./

RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# expose port 8080 to the host
EXPOSE 8080

CMD ["npm", "run", "serve"]