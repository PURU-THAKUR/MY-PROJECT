package com.example.yourapp.entities;

import javax.persistence.*;
import java.util.List;

@Entity
public class FinancialAdvisor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long advisorId;

    private String name;
    private String email;
    private String phoneNumber;
    private String officeLocation;

    @OneToMany(mappedBy = "advisor", cascade = CascadeType.ALL)
    private List<Client> clients;

    public FinancialAdvisor() {}

    public FinancialAdvisor(String name, String email, String phoneNumber, String officeLocation) {
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.officeLocation = officeLocation;
    }

    public Long getAdvisorId() {
        return advisorId;
    }

    // Getters and setters for other fields
}

