# SWIFT

> Swift is an online banking system, a straight forward digital service offering the fundamental financial services, that allows customers to perform various banking transactions and manage their accounts over the internet using a secure website.

# ROUTES

| API Method | Route         | Authenticated | Roles Permitted | Description  |
| ---------- |:-------------:| -------------:| --------------- |:------------:|
| POST       | /api/register | No            | User            | Register a new user with an email and password.|
| POST       | /api/login    | No            | User            | Authenticate a user   |
| GET        | /api/logout   | Yes           | User            | Log out the user      |
| POST       |  /api/accounts   | Yes           | User            | Create a new bank account for a user.    |
| GET        | /api/accounts/:accountId/balance  | Yes           | User            | Retrieve the account balance.  |
| POST        | /api/accounts/:accountId/deposit  | Yes           | User            | Deposit funds into the account.  |
| POST        | /api/accounts/:accountId/withdraw  | Yes           | User            | Withdraw funds from the account. |
| POST        | /api/accounts/:sourceAccountId/transfer/:targetAccountId | Yes           | User            | Transfer funds between two accounts (of the same user). |
| GET        | /api/accounts/:accountId/transactions | Yes           | User            | Retrieve the transaction history for an account.  |
| POST        | /api/admin/login  | Yes           | Admin            | Authenticate as an admin user. |
| GET        | /api/admin/accounts  | Yes           | Admin            | Retrieve a list of all user accounts. |
| GET        | /api/admin/accounts/:accountId:  | Yes           | Admin            | Retrieve details for a specific user account.|
| POST        | /api/admin/accounts/:accountId/freeze  | Yes           | Admin            | Freeze or block a user account. |
| GET        | /api/docs  | Yes           | Admin            | Documentation. (Swagger) |