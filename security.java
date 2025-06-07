package com.example.yourapp.entities;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

@Entity
public class Portfolio {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long portfolioId;

    private String portfolioName;
    private Date createdAt;

    @OneToOne
    @JoinColumn(name = "client_id")
    private Client client;

    @OneToMany(mappedBy = "portfolio", cascade = CascadeType.ALL)
    private List<Security> securities;

    public Portfolio() {}

    public Portfolio(String portfolioName, Date createdAt, Client client) {
        this.portfolioName = portfolioName;
        this.createdAt = createdAt;
        this.client = client;
    }

    public Long getPortfolioId() {
        return portfolioId;
    }

    // Getters and setters for other fields
}
