# LiquidPuzzle
Coding the "liquid puzzle" game in an artificial intelligence course - planning and decision-making. while finding a heuristic to solve the problem and implement it.

![image](https://github.com/OrenAviya/LiquidPuzzle/assets/98823130/287d2656-325c-4897-af0e-85926e148561)

חוקי המשחק
• פעולה הינה העברת צבע ממבחנה אחת למבחנה אחרת.
• פעולה חוקית הינה:
• העברת צבע למבחנה ריקה.
• העברת צבע על צבע זהה במבחנה שאינה ריקה, בתנאי שהמבחנה אליה מועבר
הצבע לא מלאה ויש בה פחות צבעים ממה שהוגדר בבעיה.
• סיום משחק כאשר כל הצבעים ממוינים במבחנות.
• אין חשיבות לסדר המבחנות. כל המצבים בהם כל המבחנות בעלות צבע
זהה הם מצבים שקולים.

Our first huristic is: 
\
פונקציית יוריסטיקה "עליונים אחרים", בשילוב עם "מרחק מנהטן".
היא מתבססת על הרעיון הפשוט של חישוב מספר המכלים ששלבם העליון, (או יותר) צבוע בצבע של הנוזל שנמצא בשלב השני  במבחנה שממנה רוצים להעביר נוזל.
נמצא את הצעדים האפשריים כרגע. 
נחשב עבור כל צעד-  את נקודות המרחק שלו מהפתרון. (לפי מרחק מנהטן?)
הצעד שיזכה לציון הנמוך ביותר- כלומר הקרוב ביותר, אותו נבחר.
בנוסף נעביר בעדיפות ראשונה צבע למבחנה שאינה ריקה. 
בנוסף נעביר בעדיפות עליונה צבע שתחתיו יש כמה שלבים שהם באותו צבע שנוכל להעביר את כולם הלאה למבחנה אחרת.

("other top" heuristic function, combined with "manhattan distance".
It is based on the simple idea of calculating the number of containers whose upper stage, (or more) is painted with the color of the liquid that is in the second stage in the test tube from which you want to transfer liquid.
We will find the possible steps right now.
Calculated for each step - its distance points from the solution. (by distance from Manhattan)
The step that will get the lowest score - that is, the closest one, will be chosen.
In addition, we will first transfer color to a test tube that is not empty.
In addition, we will transfer as a top priority a color under which there are several stages that are the same color so that we can transfer them all on to another test tube.)

