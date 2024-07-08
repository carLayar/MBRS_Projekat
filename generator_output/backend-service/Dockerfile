# Base image with JDK and Gradle
FROM gradle:7.5.0-jdk17 as build

# Set working directory
WORKDIR /home/backend-service

# Copy build files
COPY build.gradle settings.gradle /home/backend-service/
COPY src /home/backend-service/src

# Build the project
RUN gradle build --no-daemon

# Using OpenJDK 17 for the runtime
FROM openjdk:17-slim

ARG SERVICE_NAME="backend-service"

# Set the deployment directory
WORKDIR /app

# Copy the built JAR from the previous stage
COPY --from=build /home/backend-service/build/libs/$SERVICE_NAME.jar /app/app.jar

# Expose the port
EXPOSE 8080

# Define the entry point
ENTRYPOINT ["java", "-Xms256m", "-Xmx3072m", "-jar", "app.jar"]
