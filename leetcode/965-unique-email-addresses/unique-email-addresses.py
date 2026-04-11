class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            splited_email = email.split("@")
            name = ""
            for i in splited_email[0]:
                if i == '+':
                    break
                elif i != '.':
                    name += i
            new_email = name + "@" + splited_email[1]
            email_set.add(new_email)
        return len(email_set)
        