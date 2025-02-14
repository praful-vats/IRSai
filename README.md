# IRSai
### **AI-Powered Incident Detection & Log Ingestion System**  

IRSai is a **real-time, AI-driven incident detection platform** designed to ingest logs at scale, identify anomalies, and trigger automated alerts. Built for **high availability, scalability, and efficiency**, it integrates seamlessly with third-party monitoring tools and cloud infrastructure.  

---

## Key Features  
 **Real-time Log Ingestion** – Kafka-based log streaming for high-throughput processing  
 **AI-Powered Incident Detection** – ML-based anomaly detection for proactive monitoring  
 **Automated Alerts & Notifications** – WebSocket-based instant updates and third-party integrations  
 **Scalable Microservices Architecture** – Distributed processing with containerized services  
 **Celery Task Processing** – Background job execution for incident management  
 **AWS EKS Deployment** – Kubernetes orchestration for fault tolerance and high availability  

---

## Tech Stack  

### **Backend Services**  
- **Python (FastAPI)** – API services and background processing  
- **Kafka** – Distributed log ingestion for real-time streaming  
- **Celery** – Asynchronous task execution for automated workflows  
- **PostgreSQL** – Persistent storage for structured incident data  
- **Redis** – In-memory cache and real-time WebSocket notifications  

### **Infrastructure & DevOps**  
- **Docker & Docker Compose** – Containerized microservices  
- **Kubernetes (AWS EKS)** – Cloud-native orchestration and scaling  
- **AWS RDS (PostgreSQL)** – High-performance managed database  
- **AWS S3** – Storage for logs and backup data  
- **Nginx** – Reverse proxy for efficient request handling  

---
