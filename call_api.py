# Example request to access private route! 

import http.client
conn = http.client.HTTPConnection("0.0.0.0:5000")
headers = { 'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik4wVTRSVEJHTXpKRlFrRkNSRFU0TURjNFFrUTVNamhETlRCRE1qRTROalU1TWpVd1JqYzBPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xZHlpMTJoZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiVllJVDFoVEI3UGs3dE9aV28xNVN6R1c1cHJTbjNveTZAY2xpZW50cyIsImF1ZCI6ImZsYXNrdGVtcGxhdGUiLCJpYXQiOjE1NjI2ODUxMjcsImV4cCI6MTU2Mjc3MTUyNywiYXpwIjoiVllJVDFoVEI3UGs3dE9aV28xNVN6R1c1cHJTbjNveTYiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.OMF_OlmQftdLjoRolYxlvHbSAC5lh7YPuUT4p1oFX55vnjXSY7RIiicS8Tgme9vMlLacZOEJcfsfHZB01mIIJMr1AKz9dlU3nvBg67_3QEGh2RkwWStG0YY7y69gVJtlavwCEnkvDVPpZvMlR-iJyyg893dkKZKgPhvStIsHht30Bl9BvZ-t2g3knWAh0dAs0xiEUaIo8eT2Bk_28Dy6KrNSpta7eo5QgcvloUNAaAjAZJGG_sI7nAkrgNH8IqIBwKrOOu2DZpDNbaeeAIuOaeueP4SrECDBpI1UxittI0tidDBK6S0_wxruxQCGvFsNwJr2e1fcKtVP4Gy-7z8Ztw" }
conn.request("GET", "/private", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))