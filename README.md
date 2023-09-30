# Kaizen Kingdom

Website now [LIVE](https://kaizen-kingdom-7933fecd6f94.herokuapp.com/)! Hosted on Heroku.

This is version 1.0 of the platform. Please read on to find out about upcoming features.

Welcome to Kaizen Kingdom! Our mission is to empower learners by providing a comprehensive and user-friendly Learning Management System. With our platform, you can explore and master a wide range of subjects, unlocking your potential to learn anything you desire. Join us on this exciting journey of knowledge and growth!

Derived from the Japanese concept of continuous improvement, our project is built upon the belief that learning is the catalyst for personal growth and advancement. By cultivating a vibrant community of individuals who yearn to better themselves through knowledge, we establish a dynamic "kingdom" of like-minded learners.

## User Stories

In terms of user stories, there should be an overarching Theme which is divided into Epics, and further divided into User Stories. This section should consist of smaller user stories, divided by Themes and Epics. These user stories should represent a bite-sized increment, and should be prioritised and assigned to iterations. One iteration can take 1-4 weeks and can include the implementation of multiple increments.

Epics are large items that cannot fit into a single iteration, but can be broken down into user stories. Themes are a way to group together related Epics. For example, Theme: Account Management, Epic 1: User Profile, Epic 2: Sign-in, etc.

--

User Story Templates

As a [role], I can [capability], so that [received-benefit].

In order to [receive-benefit] as a [role], I can [goal/desire].

Examples:

As a warehouse employee, I can select  the paper size on which to print  
so that the printed label  size matches the parcel size.

In order to check-out multiple items in one click as a user, I can add items to a shopping cart.

--

I want my student users to have this kind of experience when they log on to Kaizen Kingdom.

When the student lands on the main page, They can click on the login button, taking them to the login page. They will use their details to log in and will be welcomed by the courses they are currently enrolled on. A student can click on a course and they will be presented with the course page which include all modules. From there they can see their progress in all modules and click on a module to begin learning. Once they do, they will be taken to a page where they are shown details on the module, with what they will learn etc. Then they will be able to see some worked examples and then be presented with questions.

## Application of Product

This is one way I can see the product working:

1. Kaizen Kingdom Website:

- Serve as the main platform for the project.
- Admin users will have access to manage the system.

2. Organization Application Process:

- Organizations interested in joining Kaizen Kingdom will apply through the website.
- Application requires payment of a subscription fee based on a tiered pricing system.
- Higher-tier organizations will have access to more teacher and student accounts.

3. Organization Setup:

- Once approved, the organization needs to be set up within Kaizen Kingdom.
Admin users can create teacher and student accounts for the organization.
- An option to upload an excel spreadsheet for bulk account creation could be provided.
- Alternatively, a 1-click download feature can generate an excel spreadsheet with login information for all users.

4. Account Management:

- Teacher accounts will have the ability to view and change passwords for students within their school.
- Students will be able to view and change their own passwords.

5. Organization Name Change:

- Organizations can submit a name change request, subject to availability.
- Name changes will be reflected throughout the organization.
- Each organization will have an associated ID for identification purposes.

6. Teacher Features:

- Teachers can create syllabi and develop questions for assessments.
- Consider the possibility of including programmable questions with randomized numbers and automatically generated answers.

7. Authentication:

- Implement authentication mechanisms to ensure different access levels for student, teacher, and admin users.
- Each user type will have access to specific features and functionalities.

## Technology Rationale

### Full Stack

Since this project is being created to be assessed by Code Institute, it must be full stack, as per the criteria. However, there are several other reasons why this is an appropriate project to create a fullstack application.

1. End-to-End Control: By creating a full-stack project, I have complete control over both the frontend and backend aspects of my LMS. This empowers me to customize and fine-tune every detail to perfectly align with my specific requirements.

2. Flexibility and Scalability: A full-stack project provides the flexibility to adapt and scale my LMS as needed. I can easily incorporate new features, modules, or integrations into both the frontend and backend layers, ensuring my LMS grows and evolves alongside my users' needs.

3. Enhanced Performance: Developing the frontend and backend components in tandem allows me to optimize performance across the entire system. I can implement efficient data retrieval and processing, minimize network requests, and optimize user interactions for a seamless and responsive experience.

4. Improved Security: With a full-stack approach, I can implement robust security measures at both the frontend and backend layers. I can employ best practices such as authentication, authorization, data encryption, and input validation to protect user data and ensure the integrity of my LMS.

5. Better User Experience: By having control over both frontend and backend components, I can design and implement a user interface (UI) that is intuitive, user-friendly, and tailored to the specific needs of my learners. This results in a more engaging and satisfying learning experience.

6. Learning Opportunities: Developing a full-stack project provides valuable learning opportunities. It allows me to gain experience in multiple technologies, frameworks, and programming languages, expanding my skill set and knowledge base, making me a more versatile and competent developer.

### Django Backend

Since Code Institute provide resources to learn the Django backend framework, it makes sense to use it in this project. However, this is not the only reason to use Django and these are some that I have researched:

1. Rapid Development: Django provides a high-level framework that enables me to develop my LMS system quickly and efficiently. Its built-in features, such as authentication, database ORM (Object-Relational Mapping), and form handling, streamline the development process and allow me to focus on implementing the core functionality of my application.

2. Scalability and Flexibility: Django's modular design and scalability make it well-suited for projects of various sizes. Whether I start with a small-scale LMS or have plans to expand and accommodate a larger user base in the future, Django's scalability ensures that my backend can handle increased traffic and growing demands.

3. Batteries-Included Approach: Django follows a "batteries-included" philosophy, offering a comprehensive set of features and tools out of the box. This includes an admin interface, user authentication, URL routing, form handling, and more. With these pre-built components, I can focus on implementing the unique aspects of my LMS system without having to reinvent the wheel.

4. Security and Authentication: Django prioritizes security and provides robust authentication mechanisms to protect user data and ensure the integrity of my LMS. It includes features like password hashing, protection against common security vulnerabilities, and user session management. With Django, I can confidently build a secure backend for my LMS application.

5. Community and Documentation: Django has a vibrant and active community, which means there is ample support and resources available when I encounter challenges or need guidance. The extensive documentation and numerous tutorials make it easier for me to learn and leverage Django's features effectively.

6. Integration and Extensibility: Django seamlessly integrates with other popular technologies, frameworks, and libraries. Whether I need to integrate with frontend libraries or frameworks like React or Next.js, utilize external APIs for additional functionality, or leverage third-party Django packages, the ecosystem around Django is rich and provides the flexibility to extend my LMS system as needed.

7. Mature and Battle-Tested: Django has been around for many years and has been extensively used in production by numerous projects and organizations. Its maturity and battle-tested nature provide me with confidence in its stability, performance, and reliability for my LMS application.

## Project Milestones

1. CRUD functionality where cards can be read, edited, created and deleted.

2. Implement a sign in feature for teachers where one can only have CRUD access when signed in. Non-users can only see the home page.

3. Create student users that only have read permissions.

4. Organise the cards into a hierarchy in terms of subject, unit, topic etc.

## Project Themes and Epics

1. User Experience
    - Responsive Design for Mobile Devices
    - Customisable User Profiles (e.g. user picture)
    - Progress Tracking
    - Achievement Badges

2. Security and Authentication
    - Secure User Registration and Login
    - Password Reset Functionaility
    - User Roles and Permissions

3. Content Management
    - Course Creation
    - Course Update Feature
    - File Management

4. Reporting and Analytics
    - Track Learner Progress
    - Teachers Able to View Student Progress


## Planning

### Strategy

For the strategy, I explored various potential features for the LMS and attempted to assess the importance and viability of their implementation.

Potential Features:

- Create Course, Unit and Topics
- Read Topics
- Update Courses with new content
- Delete Courses
- Registration and Login
- Permissions for Students and Teachers
- Track Student progress
- Allow Teachers to view Student progress
- Allow Teachers to create quizzes for their own course
- Complete Topics by passing a quiz

| Opportunity / Problem | Importance | Viability | Difficulty |
|---|:---:|:---:|:---:|
| Create Course, Units, Topics | 5 | 5 | 1 |
| Read Topics | 5 | 5 | 1 |
| Update Course content | 5 | 5 | 1 |
| Delete Course content | 5 | 5 | 1 |
| Registration and Login | 5 | 5 | 3 |
| Permissions for Visitors, Students, Teachers | 4 | 5 | 2 |
| Track Student progress | 2 | 3 | 2 |
| Allow Teachers to view Student progress | 2 | 3 | 2 |
| Allow Teachers to create quizzes | 3 | 4 | 2 |
| Complete Topics by passing a quiz | 3 | 4 | 2 |

Comparing the scores of Importance and Viability tells me I can implement all these features.

### Scope

The Scope of the project is determined based on the difficulty of implementation. As the difficulty of all features is low, they can be implemented.

### Structure

This is the ideal structure of the database:

![Database](/static/images/database.png)

This database is intended to be implemented in a modular manner with different features being addes with each release of the project.

### Skeleton

The Skeleton gives us and idea of what the frontend should look like once the project is complete. These were the wireframes generated:

![Home - Desktop - Guest](/static/images/home-desktop-guest.png)
![Home - Desktop - User](/static/images/home-desktop-user.png)
![Dashboard - Desktop - Student](/static/images/dashboard-desktop-student.png)
![Create Course - Desktop](/static/images/create-dourse-desktop.png)
![Photography - Desktop](/static/images/photography-desktop.png)
![Photography Topic - Desktop](/static/images/photography-topic-desktop.png)
![Photography Topic Edit - Desktop](/static/images/photography-topic-edit-desktop.png)
![Photography Topic New - Desktop](/static/images/photography-topic-new-desktop.png)
![Subject - Desktop - Student](/static/images/subject-desktop-student.png)
![Unit - Deskto - Student](/static/images/unit-desktop-student.png)
![Topic - Desktop - Student](/static/images/topic-desktop-student.png)
![Topic - Desktop - Student - Modal](/static/images/topic-desktop-student-modal.png)
![Worksheet - Desktop - Student](/static/images/worksheet-desktop-student.png)

### Surface

Several aspects of the surface were given some deep thought. One idea that was landed on early was the colour scheme. For this project, I was inspired by amourliquide.com with their combination of yellow, cyan and red. Specifically, the colours are as follows:

- yellow: #F7CD46
- cyan: #5AC3B0
- red: #DE5935

As for fonts, I wanted to go for a modern style and so adopted a sans-serif style.

