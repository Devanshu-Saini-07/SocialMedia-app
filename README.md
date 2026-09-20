# SocialMedia — Django Social Media Web Application

## PROJECT OVERVIEW
SocialMedia is a full-featured social media platform built using Django. It allows users to connect, share posts (text and images), follow other users, interact via likes and comments, and engage in private messaging.

## FEATURES
- **User Authentication**: Secure Signup, Login, and Logout functionality.
- **User Profiles**: View profiles, update profile information (if extended).
- **Post Management**: Create text-only or image-based posts. Edit/Delete your own posts.
- **Home Feed**: View posts from all users.
- **Social Graph**: Follow/Unfollow users; view Followers and Following lists.
- **Interactions**: Like and Comment on posts.
- **Notifications**: Stay updated with interactions (likes, comments, follows).
- **Messaging**: Private 1-to-1 conversations between users.
- **Search**: Search for users by username and posts by content.
- **Django Admin**: Built-in, secure administrative interface.
- **Responsive UI**: Fully responsive design using Bootstrap 5.

## TECH STACK
- **Backend Framework**: Python, Django 6.0.7
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Bootstrap Icons

## PROJECT STRUCTURE
```
SocialMedia-app/
├── accounts/
├── posts/
├── feed/
├── interactions/
├── follows/
├── notifications/
├── messaging/
├── search/
├── templates/
├── static/
├── media/
├── social_media/
├── manage.py
└── README.md
```

## APPLICATION MODULES
- `accounts`: Handles user authentication, profiles, and registration.
- `posts`: Manages post creation, editing, and deletion.
- `feed`: Manages the main home feed display.
- `interactions`: Handles likes and comments functionality.
- `follows`: Manages follow/unfollow relationships.
- `notifications`: Handles system notifications for interactions.
- `messaging`: Manages 1-to-1 private messaging.
- `search`: Handles username and post search functionality.

## INSTALLATION
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd SocialMedia-app`
3. Create a virtual environment: `python -m venv myenv`
4. Activate the virtual environment: `.\myenv\Scripts\Activate.ps1`
5. Install dependencies: Run `pip install -r requirements.txt` (or install via `pip install django pillow`)
6. Run migrations: `python manage.py migrate`
7. Create an admin user: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## RUNNING THE PROJECT
Once the server is started, open your web browser and navigate to:
`http://127.0.0.1:8000/`

## ADMIN PANEL
Manage the application content via the Django Admin interface at:
`/admin/`

## MAIN ROUTES
- `/`: Home Feed
- `/feed/`: Home Feed
- `/login/`: User Login
- `/signup/`: User Signup
- `/notifications/`: User Notifications
- `/messaging/`: Private Messages
- `/search/`: Search Users and Posts
- `/admin/`: Admin Panel

## SECURITY
- **Django Authentication**: Integrated auth system.
- **CSRF Protection**: Enabled on all forms.
- **Login-required**: Redirection on protected pages/actions.
- **Permissions**: Object-level ownership checks (edit/delete) implemented in views.
- **Isolation**: Notifications and Messages are user-isolated.

## FUTURE IMPROVEMENTS
- Feed pagination
- Notification pagination
- Real-time messaging (e.g., using WebSockets)
- Additional UI enhancements
- Production deployment configuration (e.g., PostgreSQL, Gunicorn, Nginx)

## TESTING
The application has undergone a final audit:
1. `python manage.py check`: Verified consistent configuration.
2. Manual Testing: Full verification of authentication, post handling, social interaction, and navigation flows.

## SCREENSHOTS
*Screenshots can be added here.*
