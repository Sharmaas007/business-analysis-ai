---
summary: GHCP: User can create a task
issueType: Story
labels:
  - AI generated
storyPoints: 2
description: |
  As a user, I want to create a task by entering a title and description so that I can track my work items.
acceptanceCriteria:
  - Given I am on the task tracker UI, when I click "Create Task", then I can enter a title and description for a new task.
  - Given I have entered valid details, when I submit the form, then the new task appears in the task list with status "pending".
---

---
summary: GHCP: User can view all tasks
issueType: Story
labels:
  - AI generated
storyPoints: 2
description: |
  As a user, I want to view all my tasks in a list so that I can see what work needs to be done and track progress.
acceptanceCriteria:
  - Given I have created tasks, when I open the task tracker, then I see a list of all tasks with their title, description, and status.
  - Given I have no tasks, when I open the task tracker, then I see an empty state message.
---

---
summary: GHCP: User can mark tasks as completed
issueType: Story
labels:
  - AI generated
storyPoints: 2
description: |
  As a user, I want to mark a task as completed so that I can keep track of finished work.
acceptanceCriteria:
  - Given I have a task in the list, when I mark it as completed, then its status updates to "completed" in the UI.
  - Given I have completed tasks, when I view the task list, then completed tasks are visually distinguished from pending tasks.
---

---
summary: GHCP: Tasks persist using local storage
issueType: Story
labels:
  - AI generated
storyPoints: 2
description: |
  As a user, I want my tasks to be saved locally so that they are available even after I close or refresh the application.
acceptanceCriteria:
  - Given I have created tasks, when I refresh or reopen the application, then my tasks are still available.
  - Given I delete my browser data, when I open the application, then my tasks are no longer available.
---

---
summary: GHCP: Application has a simple and lightweight UI
issueType: Story
labels:
  - AI generated
storyPoints: 2
description: |
  As a user, I want the application to have a simple and lightweight UI so that it is easy to use and loads quickly.
acceptanceCriteria:
  - Given I use the application, when I navigate between screens, then the UI is responsive and uncluttered.
  - Given I use the application, when I perform actions, then the interface remains fast and intuitive.
---
