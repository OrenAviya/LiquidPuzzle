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
פונקציית יוריסטיקה "עליונים אחרים" עבור משחק Liquid Puzzle.

היא מתבססת על הרעיון הפשוט של חישוב מספר המכלים ששלבם השני העליון, (או יותר) צבוע בצבע של הנוזל שעומדים להעביר.
בנוסף נעביר בעדיפות ראשונה צבע למבחנה שאינה ריקה 
בנוסף נעביר בעדיפות עליונה צבע שתחתיו יש כמה שלבים שהם באותו צבע שנוכל להעביר את כולם הלאה למבחנה אחרת. 
("Other top" heuristic function for Liquid Puzzle game.

It is based on the simple idea of calculating the number of containers whose upper second stage, (or more) is painted with the color of the liquid that is going to be transferred.
In addition, we will first transfer color to a test tube that is not empty
In addition, we will transfer as a top priority a color under which there are several stages that are the same color so that we can transfer them all on to another test tube.)

