contacts = {}
contacts = {
    "contact_1":{
    "name":"Anna Ivanova",
    "phone":"+79001234567",
    "email":"anna.ivanova@example.com"
    },
    "contact_2":{
    "name":"Petr Sidorov",
    "phone":"+79119876543",
    "email":"petrsidorov@example.com"
    }
}
print(f"All info about Anna Ivanova:{contacts['contact_1']}")
contacts['contact_2']['phone'] = "+79225551122"
contacts['contact_1']['address'] = "city Moscow, st. Pushkin, 10"
del contacts['contact_2']['email']
print(contacts)
