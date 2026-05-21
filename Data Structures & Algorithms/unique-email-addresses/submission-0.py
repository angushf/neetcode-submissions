class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for i in range(len(emails)):
            dirtyEmail = emails[i]
            dirtyEmailArray = dirtyEmail.split('@')
            dirtyEmailName = dirtyEmailArray[0]
            dirtyEmailDomain = dirtyEmailArray[1]

            cleanEmailName = ""

            for i in range(len(dirtyEmailName)):
                if dirtyEmailName[i] == ".":
                    continue
                
                if dirtyEmailName[i] == "+":
                    break

                cleanEmailName += dirtyEmailName[i]

            cleanEmail = cleanEmailName + "@" + dirtyEmailDomain
            uniqueEmails.add(cleanEmail)

        

        return len(uniqueEmails)