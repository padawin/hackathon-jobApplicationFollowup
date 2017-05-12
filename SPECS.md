# Specs

## Features

### Job Position

- creation of job position with description and name (API/WEB)
- paginated list of job positions (API/WEB)
    - For each Job Position, the User can update it, see its details, or close
      it.
- get job position info from ID (API/WEB)
    - Job position info will list also paginated the applications (API/WEB)
    - For each Job Application, the User can either download the CV, approve the
      Job Application, or reject it.

### Job Application

- A Job Application can be created with a Job Position ID, a candidate name, a
  candidate email and a CV (PDF)
- When a Job Application is accepted or rejected, an email must be sent to the
  candidate. An email must also be sent when a Job Position is closed.
