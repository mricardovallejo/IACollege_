package com.learnreactivespring;

import io.micrometer.core.annotation.Timed;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;

@Configuration
//@EnableAdminServer
@Timed
@SpringBootApplication
public class 	LearnReactivespringApplication {

	public static void main(String[] args) {
		SpringApplication.run(LearnReactivespringApplication.class, args);
	}
}
