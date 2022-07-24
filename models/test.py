# <form action="/book/checkout/{{book.title}}" method="POST">
    
    
#     <input type="submit" value="Loan">
    
#     <a href="/book_list">Back</a>
import datetime

date=datetime.date.today()
delta=datetime.timedelta(days=50)
new_date=date+delta
print(new_date)