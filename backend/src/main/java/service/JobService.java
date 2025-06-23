package com.jobmatcher.service;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class JobService {

    RestTemplate restTemplate = new RestTemplate();

    public Map<String, Object> parseResume(MultipartFile resume) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        HttpEntity<MultipartFile> request = new HttpEntity<>(resume, headers);
        ResponseEntity<Map> response = restTemplate.postForEntity("http://localhost:8000/parse-resume", request, Map.class);
        return response.getBody();
    }

    public Object fetchJobs(String skills) {
        return restTemplate.getForObject("http://localhost:8001/search?skills=" + skills, Object.class);
    }
}
