## API DOC

You can find all the APIs that are used in the JustAsk! app in this document.
Note: A Slug is the unique identifying part of a question instance.


### /api/user
GET - Displays the username of the user
![User API](/api-pic/1.User.JPG)

### /api/questions/
GET - Displays all the questions
POST - Uploads a new question
![Questions API](/api-pic/2.Question List.JPG)

### /api/questions/{slug}/
GET - Displays the details of a question instance
PUT - Edits the contents of a question instance
DELETE - Deletes a question instance
![Question API](/api-pic/3.QuestionInstance.JPG)

### /api/questions/{slug}/answers/
GET - Displays all the answers of a question instance
![Question Answers API](/api-pic/4.AnswerList.JPG)

### /api/questions/{slug}/answer/
POST - Adds a new answer of a question instance
![Add Answer API](/api-pic/5.AnswerQuestion.JPG)

### /api/answers/{answer ID}/
GET - Displays the details of an answer instance
PUT - Edits the contents of a answer instance
DELETE - Deletes a answer instance
![Answer API](/api-pic/6.AnswerRUD.JPG)

### /api/answers/{answer ID}/like/
POST - Likes the answer
DELETE - Unlikes the answer
![Like Answer API](/api-pic/7.LikedAnswer.JPG)