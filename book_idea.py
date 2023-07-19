import csv
import pandas as pd
from pyvis.network import Network
import networkx as nx




def create_graph():

    net = Network(height="100vh", width="100%", bgcolor="#222222", font_color="white")

    def edge(start, stop):
        if start == stop:
            return False
        for i in range(start, stop):
            # print(start, i+1)
            net.add_edge(start, i+1)
        return edge(start+1, stop)

    # net.add_node(0, label='МОЖЛИВО ВСЕ', size=30, x=60, y=60)

    # Розділ №1 (by Tasha Musienko)
    net.add_node(1, label='Криза – це період прихованих можливостей, це період, коли у кожного є шанс на успіх і тільки ти вирішуєш як діяти в цих умовах – змиритися, страждати…або рухатися вперед! Наші рішення визначають наше майбутнє! ', size=15)
    net.add_node(2, label='Единий спосіб зрозуміти межі можливого - вийти за них, досягаючи неможливого', size=15)

    # net.add_edge(0, 1)
    # net.add_edge(0, 2)

    # edge(1, 2)


    # Розділ №2 (Сергій Леонов)
    net.add_node(3, label='Удача посміхається тому, хто вірить', size=15)
    net.add_node(4, label='Процвітання - це постійний розвиток', size=15)
    net.add_node(5, label='Не живи за звичкою - прагни нового', size=15)
    net.add_node(6, label='Поважай себе, цінуй свої досягнення', size=15)
    net.add_node(7, label='Зміни - це страх, проте- це двері у світ можливостей', size=15)
    net.add_node(8, label='Вийти із зони комфорту - це найкраща стратегія успіху', size=15)

    # net.add_edge(2, 3)
    # net.add_edge(0, 3)
    # net.add_edge(0, 4)
    # net.add_edge(0, 5)
    # net.add_edge(0, 6)
    # net.add_edge(0, 7)
    # net.add_edge(0, 8)
    # edge(3, 8)


    # Розділ №3 (Костя Беляєв)
    net.add_node(9, label='Мисли позитивно', size=15)
    net.add_node(10, label='Перебори обмежуючі переконання', size=15)
    net.add_node(11, label='Виходь із зони комфорту та розширюй межі можливостей', size=15)
    net.add_node(12, label='Людина може змінюватися', size=15)
    net.add_node(13, label='Ми і наші результати – це не одне й те саме', size=15)
    net.add_node(14, label='Слова, які ми використовуємо для передачі думок, відображають наше ставлення до себе, інших і всього навколишнього світу', size=15)
    net.add_node(15, label='Слідкуй за тим, які люди й речі тебе оточують', size=15)

    # net.add_edge(8, 9)
    # net.add_edge(0, 9)
    # net.add_edge(0, 10)
    # net.add_edge(0, 11)
    # net.add_edge(0, 12)
    # net.add_edge(0, 13)
    # net.add_edge(0, 14)
    # net.add_edge(0, 15)
    # edge(9, 15)


    # Розділ №4 (Ірина Світлична)
    net.add_node(16, label='Успіх приходить не випадково, а як результат зусиль і планування з боку самої людини. Й однією з найважливіших складових цього планування є постановка цілей.', size=15)
    net.add_node(17, label=' Не всі цілі допомагають досягати успіху. Реалізованими і плідними найчастіше виявляються пріорітетні цілі.', size=15)
    net.add_node(18, label='Пріоритетна мета – це мета, заснована на цінностях і сформульована за системою S.M.A.R.T.', size=15)

    # net.add_edge(15, 16)
    # net.add_edge(0, 16)
    # net.add_edge(0, 17)
    # net.add_edge(0, 18)
    # edge(16, 18)


    # Розділ №5 (Денис Кошевий)
    net.add_node(19, label='Дотримуватися чіткого плану дій.', size=15)
    net.add_node(20, label='Зібрати як можна більше інформації поставленої мети.', size=15)
    net.add_node(21, label=' "Рух зі швидкістю 1%"', size=15)
    net.add_node(22, label='Не відкладати справи на завтра', size=15)

    # net.add_edge(18, 19)
    # net.add_edge(0, 19)
    # net.add_edge(0, 20)
    # net.add_edge(0, 21)
    # net.add_edge(0, 22)
    # edge(19, 22)



    # Розділ №6 (Катя Міщук)
    net.add_node(23, label='В житті людини існує 8 СФЕР, які важливі для кожного і пов’язані між собою: духовний розвиток, фінансовий добробут, відпочинок, сім’я, соціальна взаємодія, розвиток та освіта, здоров’я, кар’єра та професійне зростання', size=15)
    net.add_node(24, label='«Думай – на довго, плануй – на коротко».', size=15)
    net.add_node(25, label='Створення і виконання планів – це ключ до реалізації поставлених цілей', size=15)

    # net.add_edge(22, 23)
    # net.add_edge(0, 23)
    # net.add_edge(0, 24)
    # net.add_edge(0, 25)
    # edge(23, 25)



    # Розділ №7  (by Dmytro Cherevko)
    net.add_node(26, label='Маючи чітку мету і доклавши усю силу волі - звичку можна змінити', size=15)
    net.add_node(27, label='Дії ґрунтуються на рішеннях, а рішення передбачають рух уперед', size=15)
    net.add_node(28, label='Якщо ви хочете домогтися успіху і на шляху до нього не маєте невдач – це не нормально.', size=15)
    net.add_node(29, label='Невдача не означає, що ви нічого не досягли, – вона означає, що ви чогось навчилися.', size=15)

    # net.add_edge(25, 26)
    # net.add_edge(0, 26)
    # net.add_edge(0, 27)
    # net.add_edge(0, 28)
    # net.add_edge(0, 29)
    # edge(26, 29)


    
    # "Можливо все" Розділ №8 (стор.98-11) by Mykyta Ozernyi
    net.add_node(30, label='Не варто зволікати, вирішуйте проблему негайно', size=15)
    net.add_node(31, label='Адекватно оцініть проблему й пов’язані з нею обставини', size=15)
    net.add_node(32, label='Концентруйтеся на перевагах і задоволеннях, які приносить вам вирішення проблеми', size=15)
    net.add_node(33, label='Просіть допомоги', size=15)
    net.add_node(34, label=' Учіться на проблемах', size=15)

    # net.add_edge(29, 30)
    # net.add_edge(0, 30)
    # net.add_edge(0, 31)
    # net.add_edge(0, 32)
    # net.add_edge(0, 33)
    # net.add_edge(0, 34)
    # edge(30, 34)



    # Розділ №9  (by Vladyslav Lomaka)
    net.add_node(35, label='Керування часом допоможе вам довести почате до кінця!' , size=15)
    net.add_node(36, label='Уміння поставити цілі й знайти для них місце у вашего графіку допомагає доводити почате до логічного кінця, втілювати задумане в життя.', size=15)
    net.add_node(37, label='Керування часом починається з керування самим собою.', size=15)
    net.add_node(38, label='Вміння мріяти – це вміння ставити перед собою нові цілі, тобто не миритися з собою «нинішнім», а фантазувати про себе «завтрашнього»', size=15)

    # net.add_edge(34, 35)

    # net.add_edge(0, 35)
    # net.add_edge(0, 36)
    # net.add_edge(0, 37)
    # net.add_edge(0, 38)
    # net.add_edge(38, 1)
    # edge(35, 38)

    edge(1, 38)



    net.repulsion(
        spring_length=400,
        node_distance=700,
    )

    net.show('book-9.html', notebook=False)

def main():
    create_graph()
    # g = Network(height="100vh", width='100%')
    # g.add_nodes([1,2,3], value=[10, 100, 400],
    #                      title=['I am node 1', 'node 2 here', 'and im node 3'],
    #                      x=[50, 150, 200],
    #                      y=[50, 150, 200],
    #                      label=['NODE 1', 'NODE 2', 'NODE 3'],
    #                      color=['#00ff1e', '#162347', '#dd4b39'])

    # g.show('res.html', notebook=False)

if __name__=="__main__":
    main()



