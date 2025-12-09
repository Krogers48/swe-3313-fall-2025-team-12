# The Circuit Breakers  

Welcome to the project repository for **Team 12 – The Circuit Breakers**.  
Here you will find all of the artifacts, documentation, presentations, and source code for our **SWE 3313 Fall 2025** class project.  

We are creating an **e-commerce web application** using **Python (Flask 3.1)** and **JSON** for data storage.  
Our store will specialize in selling **TI mmWave Radars**, each as a unique, one-of-a-kind inventory item.  

---

## Meet Our Team  

| Name | KSU Email | Role |
|------|------------|------|
| **[Aashni Patel](mailto:apate301@students.kennesaw.edu)** | [apate301@students.kennesaw.edu](mailto:apate301@students.kennesaw.edu) | UI/UX Lead |
| **[Kade Rogers](mailto:kroge101@students.kennesaw.edu)** | [kroge101@students.kennesaw.edu](mailto:kroge101@students.kennesaw.edu) | Technical Lead / Architect |
| **[Nathan Rupp](mailto:nrupp1@kennesaw.view.usg.edu)** | [nrupp1@kennesaw.view.usg.edu](mailto:nrupp1@kennesaw.view.usg.edu) | Implementation Lead (Full-stack) |
| **[Sulaiman Shaikh](mailto:sshaik16@students.kennesaw.edu)** | [sshaik16@students.kennesaw.edu](mailto:sshaik16@students.kennesaw.edu) | Project Manager; Requirements & QA Co-Lead; Technical Support / Architect |
| **[Ben Sollicito](mailto:bsollici@students.kennesaw.edu)** | [bsollici@students.kennesaw.edu](mailto:bsollici@students.kennesaw.edu) | Technical Lead / Architect; Requirements & QA Co-Lead (Business Analyst) |

**Team Repository:** [https://github.com/Krogers48/swe-3313-fall-2025-team-12](https://github.com/Krogers48/swe-3313-fall-2025-team-12)

**Project Folder Structure:**  
```
/
├── implementation/
│   └── README.md
│
├── project-plan/
│   ├── resumes/
│   │   ├── aashni-patel-resume.md
│   │   ├── kaden-rogers-resume.md
│   │   ├── nathanial-rupp-resume.md
│   │   ├── sulaiman-shaikh-resume.md
│   │   └── benjamin-sollicito-resume.md
│   ├── team-assignments/
│   │   └── README.md
│   ├── technology-selection/
│   │   └── README.md
│   ├── gantt-chart/
│   │   ├── ganttproject.gan
│   │   └── gantt-chart.png
│   └── README.md
│
├── requirements/
│   ├── README.md
│   ├── use-case.md
│   ├── use-case.png
│   ├── decision-table.md
│   ├── decision-table.png
│   ├── decision-table-code-demo.py
│   ├── decision-table-code-demo-1.png
│   ├── decision-table-code-demo-2.png
│   ├── decision-table-code-demo-3.png
│   ├── decision-table-code-demo-4.png
│   ├── decision-table-code-demo-5.png
│
├── technical-design/
│   ├── assets/
│   │   ├── Data-Examples.png
│   │   ├── Entity-Field-Descriptions.png
│   │   ├── database-seed-data.png
│   │   └── entity-relationship-diagram.png
│   └── README.md
│
├── source/
│   ├── main.py
│   ├── database.json
│   ├── requirements.txt
│   ├── .gitignore
│   │
│   ├── static/
│   │   ├── cb_logo_100px.png
│   │   ├── cb_logo_150px.png
│   │   ├── cb_logo_250px.png
│   │   ├── cb_logo_50px.png
│   │   ├── cb_logo_big_boarder.jpg
│   │   ├── user_icon.png
│   │   └── user_icon.png:Zone.Identifier
│   │
│   └── templates/
│       ├── admin.html
│       ├── cart.html
│       ├── login.html
│       ├── main.html
│       ├── registration.html
│       ├── skeleton.html
│       └── test.html
│
└── README.md
```

---

## Team Resumes  

Each team member’s résumé is stored in the [`project-plan/resumes`](./project-plan/resumes) folder.  
Click below to view them directly:

- [Aashni Patel](./project-plan/resumes/aashni-patel-resume.md)  
- [Kade Rogers](./project-plan/resumes/kaden-rogers-resume.md)  
- [Nathanial Rupp](./project-plan/resumes/nathanial-rupp-resume.md)  
- [Sulaiman Shaikh](./project-plan/resumes/sulaiman-shaikh-resume.md)  
- [Ben Sollicito](./project-plan/resumes/benjamin-sollicito-resume.md)  

---

## Team Assignments  

All team assignments are documented in the [`project-plan/team-assignments`](./project-plan/team-assignments) folder.  
You can view the current progress [here](./project-plan/team-assignments/README.md).  

---

## Technology Selection  

Our technology stack details and justification are in the [`project-plan/technology-selection`](./project-plan/technology-selection/) folder.  
You can view the writeup [here](./project-plan/technology-selection/README.md).  

---

## Project Plan  

Our detailed project plan and timeline will be available in the [`project-plan/gantt-chart`](./project-plan/gantt-chart) folder.  
You can view the [Gantt chart and presentation here](./project-plan/README.md).  
The Loom video introduction and explanation can be found [here](https://www.loom.com/share/b4b1a73dbbc742899e32ddf38ad702b6?sid=3f51d675-eb6e-4ffc-8aba-045e07ce6d4e)

---

## Requirements

Our detailed requirements will be available in the [`/requirements'](./requirements) folder.   
In the [README.md](./requirements/README.md) file of the '/requirements' folder, you will find the program requirements sorted into Versions, Epics, and Stories, allowing for an easy understanding of what we believe - based on our interview with you - you want the product to be. In this file, you can also see the priority, estimated effort, type, and description we gave all of the requirements, so you can understand how we are thinking about this application, and how long we expect it to take.   
The [use case diagram](./requirements/use-case.md) provides helpful visuals that facilitate an easy understanding of the many systems and relationships in the application, as these systems and relationships may be difficult to understand for those of a non-technical background.   
The [decision table](./requirements/decision-table.md) file contains a picture of the decision table, a link to the decision table code, and a screenshot of the code. The decision table provides a visual representation of the rules, conditions, and actions a user or admin can perform, including logging in, finding an item, purchasing an item, managing inventory, and viewing sales history repot.   
The loom video can be found [here](https://www.loom.com/share/ce034118e6414038990d3ca8db96b44c?sid=9bf8cf9f-58c0-4350-983e-8bbb5a980707)   

---

## Repository Information  

**Repository Name:** [`swe-3313-fall-2025-team-12`](https://github.com/Krogers48/swe-3313-fall-2025-team-12)  
**Instructor:** Jeff Adkisson  
**Course:** SWE 3313 — Fall 2025  
**Language:** Python 3.13  
**Framework:** Flask 3.1  
**Storage:** JSON  
  
---  
  
## User Interface Design

[High Fidelity User Interface Design (Marvel)](https://marvelapp.com/prototype/g5ajhad)  
The loom video can be found [here](https://www.loom.com/share/a42ee5435b564197ac905355b868e878)   
   
---   
   
## Technical Design  
  
Here you can find all the technical details about the project including:  
- Our entity relationship diagram
- Example data
- Which technologies we will use and why
- How we will handle authentication & authorization
- Our coding style guide
- And more.  
[Technical Design](./technical-design/README.md)   
   
---   
   
## Implementation   
   
Our implementation can be found [here](./implementation/README.md).