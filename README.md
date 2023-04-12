# Marian Portal Documentation

Marian Portal: A Centralized School System for St. Mary’s Academy of Hagonoy

A Capstone Research in partial fulfillment of the Requirement for the Subject Capstone Research

# Website Workflow & Feature List

The Portal needs to be able to have these features:

1. Attendance
2. Grade
3. E-wallet
4. Schedule
5. Online Enrollment

# GITHUB REPOSITORY

This project has a repository in Github, a well known cloud hosting Git Repository. 

Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows.

[https://github.com/Riven-py/Portal](https://github.com/Riven-py/Portal)

---

# Section 1: Front-End (HTML, CSS, Django)

This project uses standard HTML5 and CSS3 to use for the front-end of the student portal.

<aside>
💡 Front-end refers to the part of a website or application that the user interacts with directly. This includes the design, layout, and functionality of the user interface, as well as any client-side programming that is necessary to make the application work.

</aside>

It was designed in [canva.com](http://canva.com) in earlier stages of development and later on implemented in Figma.

![Untitled](Marian%20Portal%20Documentation%203c03bfa6c3844d62837d5104d8aa6e93/Untitled.png)

To string everything together to work, the team uses Django, a reputable and secure full-stack framework that powers a variety of social media platforms and services like Youtube, Instagram, Spotify, and more.

<aside>
💡 Full-stack refers to a type of software development where the developer is responsible for both the front-end (the part of the application that the user interacts with directly) and the back-end (the part of the application that handles data storage, processing, and communication).

</aside>

![Folder Structure on 4/12/2023](Marian%20Portal%20Documentation%203c03bfa6c3844d62837d5104d8aa6e93/Untitled%201.png)

Folder Structure on 4/12/2023

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'main.css'%}">
    <title>Log in</title>
    <link rel="icon" href="{% static 'favicon.ico'%}">
</head>
<body>

<!--NAV BAR START--> 

    <div class="nav">
        <div class="nav-container">
            <header class ="navbar"> 
                <div class="nav-logo">
                        <img id='logo' src="{% static 'resources/logo.png '%}">
                        <p> ST. MARY'S
                        ACADEMY OF HAGONOY</p>
                        <p id="mobile-p">ST. MARY'S <br>
                        ACADEMY</p>
                </div>
                <div class="nav-buttons">
                    <ul>
                        <li> <a href="#">About</a></li>
                        <li> | </li>
                        <button>Enroll</button>
                    </ul>
                </div>
            </header>
            </div>
        </div>
    </div>

<!--NAV BAR END-->

    <div class="login-container">
        <div class="login-block">
            <div class="login-block-grid">
                <div class="login-logo">
                    <img id="logo" src="{% static 'resources/logo.png '%}" style="width: auto;height: 15vh;">
                </div>
                <div class="login-form">
                    <form>
                    <label  id="label"for="id">Welcome Back, Ignacian Marian!</label> <br>
                    <input type="text" id="id" name="id" required minlength="6" maxlength="6" size="30vw" placeholder="Student ID"> <br>
                    <input type="password" id="password" name="password" required minlength="6" size="30vw" placeholder="Password"> <br>
                    <button class="login-button">Login</button>
                    </form>
                    <div class="login-options">
                        <div class="remember-me">
                            <input type="checkbox" name="remember" id="check-remember"> <label for="remember">Remember Me</label> 
                        </div>
                        <a>Forgot Password?</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
```

![Main Login Page](Marian%20Portal%20Documentation%203c03bfa6c3844d62837d5104d8aa6e93/Untitled%202.png)

Main Login Page

![Landing Page](Marian%20Portal%20Documentation%203c03bfa6c3844d62837d5104d8aa6e93/Untitled%203.png)

Landing Page

![Profile Page](Marian%20Portal%20Documentation%203c03bfa6c3844d62837d5104d8aa6e93/Untitled%204.png)

Profile Page

<aside>
💡 These images were taken on April 12, 2022. But production was formally done much earlier.

</aside>

With a theme and a few websites ready, the team is ready to implement a login system, that Django itself has provided.

# Section 2: User Authentication

Django provides a dedicated login system using a default set of user database entity with its attributes, but to meet specifications of the website, the team aims to create a custom user model with its own set of attributes to be more applicable to the website.

The website, in design would need the administrator of the website to register them manually and it would use their custom School ID, thus requiring the students to be enrolled to be able to use the portal.
