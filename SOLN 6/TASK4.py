book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)

for i in range(len(book_info)):
    print(f"{book_info[i][1]} won the '{book_info[i][0]}' category with {book_info[i][2]} votes")