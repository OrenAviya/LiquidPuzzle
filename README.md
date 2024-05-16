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
פונקציית יוריסטיקה "עליונים אחרים", בשילוב עם "מרחק מראש המחסנית".
נמצא את הצעדים האפשריים כרגע.)
בכל מהלך המשחק: אם יש צעד פשוט ממבחנה לא ריקה למבחנה לא ריקה אחרת נעשה אותו. רק אם יש מקום לכל רצף הצבע. 
כלומר נעביר בעדיפות ראשונה צבע למבחנה שאינה ריקה. 
כאשר נתקענו - ע"מ להעביר למבחנה ריקה נפעל לפי היוריסטיקה הבאה:
נחשב עבור כל צעד- את המרחק שלו מהפתרון. (המרחק הגדרנו למטה)
הצעד שיזכה לציון הנמוך ביותר- כלומר הקרוב ביותר, אותו נבחר. בהינתן שחייבת להתקיים מבחנה ששלבה העליון, (או יותר) צבוע בצבע של הנוזל שנמצא בשלב השני במבחנה שממנה רוצים להעביר נוזל.
אם יש תיקו נבחר את הצבע שיש ממנו יותר בשלבים העליונים של המבחנות.

בנוסף נעביר בעדיפות עליונה צבע שתחתיו יש כמה שלבים שהם באותו צבע שנוכל להעביר את כולם הלאה למבחנה אחרת.

הגדרנו שמרחק הוא: 
המרחק המצטבר של הצבע לראש המחסנית למשל אם צבע מסויים נמצא בארבא מחסניות שונות מפוזר בשלבים 1 , 2 , 3 , 4 אזי הציון "מרחק שלו" הוא 10. 
אם יש בלוק של צבע זהה בשני שלבים באותה מחסנית אחד אחרי השני אזי נחשיב רק את השלב הקרוב ביותר לראש המחסנית .

("other top" heuristic function, combined with "manhattan distance".
It is based on the simple idea of calculating the number of containers whose upper stage, (or more) is painted with the color of the liquid that is in the second stage in the test tube from which you want to transfer liquid.
We will find the possible steps right now.
Calculated for each step - its distance points from the solution. (by distance from Manhattan)
The step that will get the lowest score - that is, the closest one, will be chosen.
In addition, we will first transfer color to a test tube that is not empty.
In addition, we will transfer as a top priority a color under which there are several stages that are the same color so that we can transfer them all on to another test tube.)

