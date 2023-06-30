# Kaizen Kingdom

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

## Mascot

Introducing a mascot to this project can serve as a powerful symbol for this educational initiative. Here is why I think having a mascot is a fantastic idea:

1. Emotional Connection: A mascot instantly connects with people on an emotional level. It's like having a friendly face that everyone can relate to and feel comfortable with.

2. Brand Identity Boost: A well-designed mascot becomes the visual representation of our project. It helps us stand out from the crowd, making us memorable and recognizable.

3. Fun and Engaging: A mascot adds a lots of fun to the learning experience! It brings an element of playfulness and excitement that keeps learners engaged and motivated.

4. Positive Learning Environment: The mascot sets a positive tone for learning. It creates a welcoming atmosphere, encourages participation, and boosts morale among learners.

5. Clear Communication: The mascot can become the project's spokesperson, delivering messages and information in a relatable and engaging way. It helps simplify complex concepts and makes learning more accessible.

Having a mascot is all about injecting personality and charm into the project. It adds that extra spark that makes learning enjoyable and memorable for everyone involved.

I have chosen the charming Kitsune as the mascot for our project. Drawing inspiration from the Japanese mythological fox renowned for its wisdom and intelligence, our mascot embodies the spirit of learning and growth. Now, let's decide on the perfect name from our two options: Kaiki and Kaiko. Here's a breakdown of each name:

Kaiki: This name creatively combines the first syllables from our project's title, capturing its uniqueness and emphasizing our commitment to continuous improvement. To symbolize the mysterious and enchanting nature of our mascot, we can associate the kanji 怪奇, meaning "mysterious" or "strange," with the name Kaiki.

Kaiko: Similarly derived, the name Kaiko incorporates the "ko" syllable from the Japanese word for "kingdom" (oukoku). It represents the grandeur and scale of our project, while maintaining a touch of Japanese influence. The kanji 開光, which signifies "opening" and "enlightenment," perfectly aligns with our mascot's transformative power and the essence of education.

To ensure our decision resonates with our target audience, we will conduct market research, gathering valuable insights and preferences. Additionally, considering the gender of our mascot, if relevant, can further enhance its appeal and connection with our learners.

By combining market feedback, personal preference, and the desired branding objectives, we can confidently select the name that best captures the essence of our educational journey and creates a lasting impression.

Decision: to be determined.

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

### React Frontend

I have decided to employ the React frontend framework for my Learning Management System (LMS) project, and I believe it offers several compelling reasons to support this decision. I have personally used React before in other frontend applications but in addition, here is my rationale for using React:

1. Component-Based Architecture: React's component-based architecture allows me to break down the user interface of my LMS into modular and reusable components. This approach enhances code organization, promotes reusability, and simplifies maintenance and updates.

2. Efficient and Reactive Rendering: React's virtual DOM and efficient diffing algorithm optimize the rendering process. By updating only the necessary components when there are changes, React ensures fast and responsive user interfaces, which is crucial for delivering a smooth learning experience in my LMS.

3. Unidirectional Data Flow: React follows a unidirectional data flow pattern, making it easier to manage the state and data flow within my LMS application. With the help of state management libraries like Redux or Context API, I can ensure consistency and predictability in handling data and state changes.

4. Rich Ecosystem and Community: React has a thriving ecosystem and a large community of developers. This means there is extensive documentation, numerous libraries, and a wealth of resources available to assist me during the development process. I can leverage existing solutions, components, and patterns to accelerate my LMS project's development and ensure its success.

5. Reusability and Code Maintainability: React's component-based approach and emphasis on reusability enable me to build reusable UI elements and encapsulate complex functionality into self-contained components. This reusability simplifies code maintenance, improves readability, and reduces the likelihood of introducing bugs or inconsistencies.

6. Declarative and Readable Syntax: React's declarative syntax makes it easier to understand and reason about the UI logic. The JSX syntax, which combines JavaScript and HTML-like syntax, allows me to write expressive and readable code, enhancing collaboration among developers and making it easier to onboard new team members.

7. Support for Single-Page Applications: React is well-suited for building single-page applications (SPAs) due to its efficient rendering, routing capabilities, and state management options. By adopting React for my LMS frontend, I can create a seamless and interactive user experience, with smooth transitions between different sections and pages of the application.

8. Responsive UI with React Native: If I decide to extend my LMS to mobile platforms in the future, React Native, a framework built on top of React, allows for the development of native mobile applications using JavaScript. This potential for code sharing between the web and mobile platforms can save time and effort in maintaining consistent functionality and branding across different devices.

In conclusion, my choice to utilize the React frontend framework for my LMS project is driven by its component-based architecture, efficient rendering, unidirectional data flow, extensive ecosystem and community support, reusability, code maintainability, declarative syntax, support for SPAs, and the potential for mobile application development through React Native. These factors make React an excellent choice for building the user interface of my LMS, ensuring an engaging, interactive, and scalable learning experience for my users.

## Project Milestones

1. CRUD functionality where cards can be read, edited, created and deleted.

2. Implement a sign in feature for teachers where one can only have CRUD access when signed in. Non-users can only see the home page.

3. Create student users that only have read permissions.

4. Organise the cards into a hierarchy in terms of subject, unit, topic etc.