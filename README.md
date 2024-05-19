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

פונקצית היוריסטיקה מחשבת את המרחק בין מצב נוכחי למצב מטרה בפאזל העברת נוזלים. המרחק הוא אומדן של מספר המהלכים המינימלי הנדרש כדי להגיע מהמצב הנוכחי למצב המטרה. (בדומה למרחק מנהטן שלמדנו בשיעור)

הפונקציה פועלת על ידי איטרציה על המיכלים במצב הנוכחי ולכל נוזל במיכל, היא מוצאת את הנוזל המתאים במצב המטרה. המרחק בין המיקום הנוכחי של הנוזל למיקום המטרה שלו מתווסף לאחר מכן למרחק הכולל. הפונקציה גם מענישה את המרחק אם הנוזל הנוכחי אינו על גבי אותו נוזל במיכל.


The enhanced_heuristic function calculates the distance between a current state and a goal state in a fluid transfer puzzle. The distance is an estimate of the number of moves to reach the current condition conditions. (Similar to the Manhattan distance we studied in class)

The function iterates over the containers in the current state and for each liquid in the container, it finds the appropriate liquid for the need. The distance between the fluid's current position and its point is added after reaching the distance. The function also penalizes the distance if the current liquid is not on top of the same liquid in the tank.

בפתרון שלנו נשתמש באלגוריתם A* יחד עם פונקציית היוריסטיקה הזו. 


