package com.jobmatcher.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.beans.factory.annotation.Autowired;
import com.jobmatcher.service.JobService;

import java.util.Map;

@RestController
public class ResumeController {

    @Autowired
    JobService jobService;

    @PostMapping("/uploadResume")
    public Map<String, Object> uploadResume(@RequestParam("resume") MultipartFile resume) {
        return jobService.parseResume(resume);
    }

    @GetMapping("/searchJobs")
    public Object searchJobs(@RequestParam String skills) {
        return jobService.fetchJobs(skills);
    }
}
