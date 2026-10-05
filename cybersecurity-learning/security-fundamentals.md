# Security Fundamentals: Identity, Access & Accounts

**Status:** Introductory study guide; not a completed assessment.

## Authentication and authorization
**Authentication** checks who an entity is. Signing in is an example.  
**Authorization** determines what that entity is allowed to do.

A collaborator can be authenticated to GitHub while lacking permission to edit a particular repository. Successful sign-in does not itself grant every permission.

## Least privilege
Give a person or application the access it needs for its task. Review permissions when the task or responsibilities change. Prefer access limited to the relevant project when that meets the need.

## Passwords and MFA
- Use a unique password for each account that supports passwords.
- A password manager can help generate and store unique passwords.
- MFA uses more than one kind of authentication factor. Two different passwords alone are not two factors.
- Where supported, phishing-resistant authenticators such as passkeys bind sign-in to the legitimate origin.
- Keep account recovery methods current and recovery codes stored securely.

## API credentials
An API key or access token may grant access to a service. Its permissions depend on the service and the credential's scope. Do not place live credentials in public repositories. Use dummy values in examples and revoke a credential if it has been exposed.

## HTTP is a starting point
An HTTP response has a status code, headers and a body. A security-related header expresses one specific behaviour; it does not certify that an application is secure. The local lab demonstrates JSON responses and one header without implementing sign-in or a full security architecture.

## Reflection prompts
1. What is one example of authentication succeeding while authorization fails?
2. Which permissions would an app need to edit one repository?
3. How would I distinguish a token's scope from the identity of its owner?
4. What recovery options should I check before changing account access?

## Sources
[OWASP authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP MFA](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

[Learning index](README.md)
