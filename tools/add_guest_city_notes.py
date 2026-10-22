#!/usr/bin/env python3
"""City-note guides for every published language except en, de, ko, ja.

Four topics: a rainy day indoors, one day in the city, family or group, street food.
Slugs are guest-note-* so they cannot collide with another PR on the same topics.
Facts stay generic and local. Property details are not invented.
"""
import json, os, sys, unicodedata
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP={'en','de','ko','ja'}
EXTRA={'vi','hi','pa','ur'}  # these already publish guide/hcmc-with-family/
CJK={'zh','zh-tw'}
IDS=('guide-note-rain','guide-note-day','guide-note-group','guide-note-food')
TOPICS=('rain','day','group','food')

def S(h2, *ps, ul=None):
    d={'h2':h2}
    if ps: d['p']=list(ps)
    if ul: d['ul']=list(ul)
    return d

def page(title, description, h1, lead, sections):
    return {'title':title,'description':description,'h1':h1,'lead':lead,'sections':sections}

def A(href, text):
    return f'<a href="{href}">{text}</a>'

def L(intro, guide, mid, tg, home_html, fam=None, fam_mid=''):
    """Descriptive links: 2 guides, optional family guide, plus the home page.

    intro ends where the first anchor begins. home_html is its own sentence and
    must contain the same-language home link href="{L}".
    """
    g=A('{L}guide/', guide)
    t=A('{L}travel-guide/', tg)
    if fam:
        f=A('{L}guide/hcmc-with-family/', fam)
        return f'{intro}{g}{mid}{t}{fam_mid}{f}. {home_html}'
    return f'{intro}{g}{mid}{t}. {home_html}'

DATA={}

def add_vi():
    g,tg='cẩm nang Sài Gòn','gợi ý địa điểm cho khách ở'
    home='Ngôi nhà được giới thiệu trên <a href="{L}">trang chủ</a>.'
    fam,fam_mid='bài đi cùng gia đình',' và '
    DATA['vi']=dict(
        btn='Đặt phòng và liên hệ',
        book='Nếu bạn muốn ở lại Thành phố Hồ Chí Minh, trang đặt phòng và liên hệ cho biết cách đặt nhà.',
        more_h2='Đọc thêm trên cùng website',
        hub_h2='Bốn chủ đề cho ngày ở Sài Gòn',
        hub_p='Bốn bài dưới đây nói về ngày mưa, một ngày trong trung tâm, đi cùng gia đình hoặc nhóm, và đồ ăn vỉa hè.',
        cards=[
            ['Sài Gòn ngày mưa','guide-note-rain','Bảo tàng, chợ có mái và quán cà phê khi trời mưa.'],
            ['Sài Gòn trong một ngày','guide-note-day','Một vòng trung tâm, không cố xem hết mọi nơi.'],
            ['Sài Gòn cùng gia đình hoặc nhóm','guide-note-group','Thảo Cầm Viên, múa rối nước và bữa ăn dùng chung.'],
            ['Đồ ăn đường phố Sài Gòn','guide-note-food','Phở, bánh mì, cơm tấm và cách chọn quán vỉa hè.'],
        ],
        links={
            'rain':L('Để nối một ngày mưa với phần còn lại của chuyến đi, xem ', g, ', ', tg, home, fam, fam_mid),
            'day':L('Để ghép một ngày ở trung tâm với các ý khác, xem ', g, ', ', tg, home, fam, fam_mid),
            'group':L('Khi đi cùng gia đình hoặc một nhóm, xem ', g, ', ', tg, home, fam, fam_mid),
            'food':L('Nếu muốn thêm chỗ ăn và chỗ đi, xem ', g, ', ', tg, home, fam, fam_mid),
        },
        pages={
            'guide-note-rain':page(
                'Sài Gòn ngày mưa: ở trong nhà','Sài Gòn các tháng mưa, thường từ tháng 5 đến tháng 11, vẫn đi chơi được. Bảo tàng, Dinh Độc Lập, bưu điện, chợ có mái và quán cà phê là chỗ trú mưa.',
                'Sài Gòn ngày mưa, chơi trong nhà',
                'Mưa không có nghĩa là hủy cả ngày ở Thành phố Hồ Chí Minh. Bảo tàng, chợ có mái và quán cà phê là cách làm thường gặp.',
                [S('Những tháng hay mưa','Thành phố Hồ Chí Minh thuộc khí hậu nhiệt đới. Mưa lớn thường gặp khoảng từ tháng 5 đến tháng 11. Từ khoảng tháng 12 đến tháng 4, trời khô hơn. Sau mưa lớn, chỗ trũng có thể đọng nước một lúc rồi thoát. Trong các tháng ẩm, nên có một điểm trong nhà trong kế hoạch.'),
                 S('Chỗ ở trong nhà hoặc có mái', ul=[
                    'Bảo tàng Chứng tích Chiến tranh, Bảo tàng Mỹ thuật và Bảo tàng Lịch sử.',
                    'Dinh Độc Lập, với các phòng tiếp khách và phần trưng bày trong nhà.',
                    'Bưu điện thành phố và Nhà thờ Đức Bà nằm cùng một khu trung tâm.',
                    'Chợ Bến Thành là chợ có mái, có đồ ăn và hàng nhỏ.',
                    'Chùa Ngọc Hoàng: cởi giày và ăn mặc gọn gàng, như ở nhiều chùa khác.',
                    'Múa rối nước được diễn trong nhà.',
                    'Quán cà phê và cửa hàng có máy lạnh dùng được khi cơn mưa bắt đầu.']),
                 S('Cách xếp một ngày','Chọn một bảo tàng hoặc Dinh Độc Lập. Dành chợ có mái hoặc một quán cà phê cho lúc mưa nặng. Phố đi bộ Nguyễn Huệ để cuối ngày nếu mưa dịu. Nhà thờ, bưu điện và phố đi bộ nằm cùng khu trung tâm. Giờ mở cửa hay đổi, nên hỏi tại chỗ trước khi đi.')]),
            'guide-note-day':page(
                'Sài Gòn trong một ngày ở trung tâm','Một ngày ở Sài Gòn đủ cho khu trung tâm: Nhà thờ Đức Bà, bưu điện, phố đi bộ Nguyễn Huệ và Chợ Bến Thành, thêm một bảo tàng hoặc Dinh Độc Lập.',
                'Sài Gòn trong một ngày',
                'Một ngày ở Thành phố Hồ Chí Minh xem được khu trung tâm. Một ngày không xem hết mọi bảo tàng và mọi khu phố.',
                [S('Một vòng trung tâm','Nhà thờ Đức Bà, bưu điện thành phố, Đường Sách Nguyễn Văn Bình và phố đi bộ Nguyễn Huệ nằm cùng khu trung tâm, nên nhiều người đi bộ giữa các điểm này. Chợ Bến Thành là chỗ quen để ăn hoặc xem hàng. Nên thêm Dinh Độc Lập hoặc một bảo tàng, không cộng thêm mọi địa danh khác trong cùng ngày.'),
                 S('Đi giữa các điểm', ul=[
                    'Trong khu trung tâm, nhiều điểm nằm gần nhau nên có thể đi bộ.',
                    'Xe buýt và tuyến metro đi từ khu Chợ Bến Thành dùng cho quãng dài hơn.',
                    'Taxi và xe gọi qua ứng dụng rất phổ biến. Nhờ tài xế bật đồng hồ, hoặc xác nhận chuyến trong ứng dụng trước khi đi.',
                    'Xe máy là một phần của giao thông. Sang đường theo nhịp người đi bộ, không dừng giữa dòng xe.']),
                 S('Nên để ngày khác','Thảo Cầm Viên, một ngôi chùa, bảo tàng thứ hai, hoặc điểm ngoài thành phố như địa đạo Củ Chi, cần một ngày riêng. Trong ngày ở trung tâm, một bữa ăn đường phố và một ly cà phê là đủ. Phở, bánh mì hoặc cơm tấm đều dễ gặp. Cà phê sữa đá là kiểu uống quen.')]),
            'guide-note-group':page(
                'Sài Gòn cùng gia đình hoặc nhóm','Đi Sài Gòn cùng gia đình hoặc nhóm nên có một chỗ ngoài trời và một chỗ trong nhà: Thảo Cầm Viên, múa rối nước, một bảo tàng và một bữa ăn chung.',
                'Sài Gòn với gia đình hoặc nhóm',
                'Thành phố Hồ Chí Minh hợp với gia đình và với nhóm nếu ngày được chia giữa một điểm ngoài trời và một điểm trong nhà.',
                [S('Khi đi với trẻ em', ul=[
                    'Thảo Cầm Viên là vườn thú và thảo cầm viên lâu đời của thành phố, có lối đi có bóng cây.',
                    'Múa rối nước diễn trong nhà, dễ xem mà không cần nhiều lời thoại.',
                    'Chợ có mái rất đông. Nắm tay trẻ em gần đường và giữa các dãy hàng.',
                    'Giữa trưa thường nóng. Buổi sáng và cuối chiều hợp với ngoài trời. Giữa ngày hợp với bảo tàng, quán cà phê hoặc nghỉ.',
                    'Nên uống nước đóng chai hoặc nước đã lọc.',
                    'Ở chùa và nhà thờ, ăn mặc gọn gàng. Ở chùa thường cởi giày.']),
                 S('Khi đi một nhóm','Nhóm có thể gọi vài món nhỏ ở quán vỉa hè, hoặc vài đĩa ở quán phở hay cơm tấm. Phố đi bộ Nguyễn Huệ và khoảng trống trước Nhà hát Thành phố là chỗ hẹn buổi tối dễ tìm. Chọn một bảo tàng hoặc Dinh Độc Lập để cả nhóm ở cùng nhau, và chừa thời gian không xếp lịch thay vì nhồi mọi địa danh.'),
                 S('Ghi chú chung', ul=[
                    'Giao thông xe máy dày đặc. Sang đường cùng người khác, với nhịp đều.',
                    'Quầy nhỏ thường nhận tiền mặt. Một số chỗ cũng có mã QR để chuyển khoản.',
                    'Khoảng từ tháng 5 đến tháng 11, nên giữ sẵn một danh sách điểm trong nhà.'])]),
            'guide-note-food':page(
                'Đồ ăn đường phố ở Sài Gòn','Đồ ăn đường phố Sài Gòn có từ sáng đến tối: phở, bánh mì, cơm tấm, hủ tiếu, bánh xèo và cà phê sữa đá. Nên chọn quán thấy người ta nấu trước mặt.',
                'Đồ ăn đường phố ở Sài Gòn',
                'Bếp trên vỉa hè là cách ăn bình thường ở Thành phố Hồ Chí Minh, từ bữa sáng đến khuya.',
                [S('Món hay gặp', ul=[
                    'Phở: soup bánh phở, thường với bò hoặc gà.',
                    'Bánh mì: ổ bánh với thịt, đồ chua, rau thơm và ớt.',
                    'Cơm tấm: cơm tấm với sườn nướng, bì, chả và trứng.',
                    'Hủ tiếu và các soup sợi trong khác.',
                    'Bánh xèo: bánh giòn, ăn kèm rau.',
                    'Gỏi cuốn: cuốn tươi với rau thơm.',
                    'Chè: các món ngọt.',
                    'Cà phê sữa đá là kiểu uống quen. Bạc xỉu nhạt cà phê hơn và nhiều sữa hơn.']),
                 S('Ở quán vỉa hè','Quán đặt ghế thấp trên vỉa hè. Quán đông, món ra nhanh, là lựa chọn quen. Nên chọn chỗ nấu trước mặt bạn. Nếu muốn ít ớt, nói lúc gọi. Món chay thường được ghi chữ chay.'),
                 S('Thói quen hữu ích', ul=[
                    'Bữa sáng là giờ ăn đường phố lớn, nhất là phở và bánh mì. Buổi tối có thêm đồ nướng và ốc.',
                    'Chợ Bến Thành và nhiều tuyến phố trong khu dân cư đều có quán ngồi và quán mang đi.',
                    'Quầy nhỏ thường nhận tiền mặt. Một số chỗ có mã QR để chuyển khoản.',
                    'Chọn món được nấu trước mặt và ăn nóng. Uống nước đóng chai hoặc nước đã lọc.',
                    'Không cần tìm một cái tên nổi tiếng. Quán bình thường mà đông khách là kiểu ăn của thành phố.'])]),
        },
    )

def add_zh():
    g,tg='西贡旅游攻略','住客可用的本地地点指南'
    home='房子的介绍在<a href="{L}">首页</a>。'
    DATA['zh']=dict(
        btn='预订与联系',
        book='如果想住在胡志明市，预订与联系页说明如何预订这栋房子。',
        more_h2='本站上的其他阅读',
        hub_h2='西贡一天可以怎么过',
        hub_p='下面四篇分别写雨天、市中心一天、与家人或朋友同行，以及街头饮食。',
        cards=[
            ['西贡雨天','guide-note-rain','博物馆、有顶市场和咖啡馆，用来躲开阵雨。'],
            ['西贡一天','guide-note-day','只走市中心，不把每个景点排进同一天。'],
            ['西贡同行','guide-note-group','动物园、水上木偶和一顿大家一起吃的饭。'],
            ['西贡街头吃','guide-note-food','河粉、法棍、碎米饭，以及怎么挑路边摊。'],
        ],
        links={
            'rain':L('雨天之外的行程，可以接着看', g, '和', tg, home),
            'day':L('想把这一天和其他安排接上，可以看', g, '和', tg, home),
            'group':L('和家人或朋友一起走，可以再看', g, '和', tg, home),
            'food':L('如果还想找地方吃、找地方走，可以看', g, '和', tg, home),
        },
        pages={
            'guide-note-rain':page(
                '西贡雨天：室内怎么安排','胡志明市约五月至十一月常有大阵雨，十二月至四月较干。雨天可去战争遗迹博物馆、美术馆、独立宫、中央邮局、滨城市场或咖啡馆，水上木偶也在室内演出。',
                '西贡雨天，安排在室内',
                '下雨不必取消胡志明市的一天。博物馆、有顶的市场和咖啡馆是常见的室内安排。',
                [S('哪几个月更常下雨','胡志明市是热带气候。大约五月到十一月常有大阵雨。大约十二月到四月更常是干季。大雨之后，低洼处可能短时间积水，然后退去。湿季里，一天的安排里应该有一个室内落点。'),
                 S('室内或有顶的地方', ul=[
                    '战争遗迹博物馆、美术馆和历史博物馆。',
                    '独立宫，接待厅和展览都在室内。',
                    '中央邮局和红教堂在同一片市中心。',
                    '滨城市场是有顶的市场，有吃的，也有小商品。',
                    '玉皇殿：和许多寺庙一样，进门脱鞋，穿着朴素。',
                    '水上木偶在室内演出。',
                    '阵雨开始时，咖啡馆和有冷气的店铺可以先避一避。']),
                 S('怎样排这一天','选一座博物馆或独立宫。把有顶的市场或一家咖啡馆留给出雨最大的时候。雨势缓和的话，阮惠步行街可以放在一天的后面。教堂、邮局和步行街在同一片市中心。开放时间会变，出发前在当地确认。')]),
            'guide-note-day':page(
                '西贡一天：只走市中心','西贡的一天适合走市中心：红教堂、中央邮局、书店街、阮惠步行街和滨城市场，再加一座博物馆或独立宫。把其余景点和市外地点留到另一天。出发前请在当地确认开放时间。',
                '西贡的一天',
                '在胡志明市过一天，可以把市中心走清楚。一天覆盖不了每座博物馆和每片街区。',
                [S('市中心这一圈','红教堂、中央邮局、阮文平书店街和阮惠步行街在同一片市中心，很多人在这些点之间步行。滨城市场是吃饭或看摊位的常见一站。同一天里加上独立宫或一座博物馆即可，不必再把其余景点都排进去。'),
                 S('点与点之间', ul=[
                    '市中心这几处彼此靠近，可以步行衔接。',
                    '公共汽车，以及从滨城市场一带出发的地铁，用来走更远的距离。',
                    '出租车和在应用里叫的车很常见。可以请司机打表，或在出发前在应用里确认行程。',
                    '摩托车是路面交通的一部分。过马路时跟着行人的节奏，不要停在车流中间。']),
                 S('留给另一天','动物园、一座寺庙、第二座博物馆，以及市外的地点如古芝地道，都更适合单独的一天。市中心这一天，一顿街头餐和一杯咖啡就够。河粉、法棍或碎米饭都容易找到。炼乳冰咖啡是本地常见的喝法。')]),
            'guide-note-group':page(
                '西贡与家人或朋友同行','和家人或朋友在西贡，宜把一天分成户外和室内：动物园与植物园、室内水上木偶、一座博物馆，再加一顿一起吃的饭。中午通常很热，早晨和傍晚更适合走在户外。',
                '和家人或朋友在西贡',
                '胡志明市适合家庭，也适合朋友同行，只要这一天分成一处户外和一处室内。',
                [S('和孩子一起', ul=[
                    '西贡动物园和植物园是城里历史很长的公园，园路有树荫。',
                    '水上木偶在室内演出，对白不多也看得懂。',
                    '有顶的市场很热闹。在马路边和摊位之间拉着孩子的手。',
                    '中午通常很热。早晨和傍晚适合户外。中午适合博物馆、咖啡馆或休息。',
                    '饮用瓶装水或过滤水。',
                    '寺庙和教堂宜穿着朴素。寺庙里通常要脱鞋。']),
                 S('和朋友一起','可以在路边摊点几样小菜，或在河粉店、碎米饭店点几盘一起吃。阮惠步行街和歌剧院前的空地是晚上容易找到的会合点。选一座博物馆或独立宫，让大家待在一起，并留出没有排满的时间，而不是把每个景点都塞进同一天。'),
                 S('大家都用得上的备注', ul=[
                    '摩托车很多。过马路时与其他人保持平稳的步速。',
                    '小摊通常收现金。有的地方也放二维码，用于银行转账。',
                    '大约五月到十一月，手边留一份室内地点名单。'])]),
            'guide-note-food':page(
                '西贡街头饮食怎么吃','西贡街头从早餐吃到夜里：河粉、法棍、碎米饭、粿条、煎饼和炼乳冰咖啡。看摊主是否当面烹煮，忙的小摊是本地常见选择，小摊多收现金。不必追一个有名的招牌。',
                '西贡的街头饮食',
                '在人行道上做饭，是胡志明市从早餐到深夜都常见的吃法。',
                [S('常会遇见的吃食', ul=[
                    '河粉：米粉汤，常见牛肉或鸡肉。',
                    '法棍：面包夹肉、腌菜、香草和辣椒。',
                    '碎米饭：配烤排骨、肉松、蛋和煎蛋饼一类的小菜。',
                    '粿条，以及其他清汤粉面。',
                    '煎饼：脆皮咸饼，配大量香草。',
                    '鲜春卷：米纸卷香草。',
                    '甜汤：各式甜品。',
                    '炼乳冰咖啡是常见喝法。白咖啡更淡，奶更多。']),
                 S('在路边摊','摊主把矮凳放在人行道上。客人多、上菜快的摊是通常的选择。看食物在你面前做出来。想少放辣椒，点单时说一声。素食常常标着 chay。'),
                 S('有用的习惯', ul=[
                    '早餐是街头饮食的重要时段，尤其是河粉和法棍。晚上多了烧烤和炒螺。',
                    '滨城市场和许多街巷都有坐下来吃的摊，也有带走的。',
                    '小摊通常收现金。有的地方有二维码，用于银行转账。',
                    '选当面做熟、热着端上来的食物。饮用瓶装水或过滤水。',
                    '不必追一个很有名的招牌。普通而忙碌的摊，就是这座城市的吃法。'])]),
        },
    )

# MORE_LANGS

def width(s):
    return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in s)

def glen(s):
    return sum(1 for ch in s if unicodedata.category(ch)!='Mn')

def expected():
    return sorted(fn[:-5] for fn in os.listdir(os.path.join(ROOT,'content')) if fn.endswith('.json') and fn[:-5] not in SKIP)

def assemble(code, data):
    pages={}
    btn=data['btn']
    note=data['book']+' '+f'<a class="btn b1" href="{{L}}booking/">{btn}</a>'
    for pid, spec in data['pages'].items():
        topic=pid.removeprefix('guide-note-')
        secs=[dict(s) for s in spec['sections']]
        secs.append({'h2':data['more_h2'],'p':[data['links'][topic]]})
        secs.append({'note':note})
        pages[pid]={'title':spec['title'],'description':spec['description'],'h1':spec['h1'],'lead':spec['lead'],'sections':secs}
    return pages

def hub(data):
    return {'_guest_notes':1,'h2':data['hub_h2'],'p':[data['hub_p']],'cards':data['cards']}

def validate():
    sys.path.insert(0, os.path.join(ROOT,'tools'))
    import district_scan
    src=open(os.path.join(ROOT,'tools','check_site.py'),encoding='utf-8').read().split('import unicodedata')[0]
    ns={'__file__':os.path.join(ROOT,'tools','check_site.py')}
    exec(src, ns)
    bad, bad2=ns['bad'], ns['bad2']
    errs=[]
    exp=expected()
    if sorted(DATA)!=exp:
        errs.append('languages: have '+','.join(sorted(DATA))+' expected '+','.join(exp))
    for code, data in DATA.items():
        if set(data['pages'])!=set(IDS):
            errs.append(code+' pages '+str(sorted(data['pages'])))
        blob=[]
        pages=assemble(code, data)
        for pid, p in pages.items():
            topic=pid.removeprefix('guide-note-')
            t,d,h=p['title'],p['description'],p['h1']
            blob += [t,d,h,p['lead'], json.dumps(p['sections'],ensure_ascii=False)]
            if '!' in t+d+h+p['lead']+json.dumps(p['sections'],ensure_ascii=False) or '！' in t+d+h:
                errs.append(f'{code}/{pid} exclamation')
            for label, val in (('title',t),('h1',h),('desc',d)):
                m=district_scan.DIST.search(val)
                if m: errs.append(f'{code}/{pid} district {label}:{m.group(0)}')
            if code in CJK:
                if len(t)>60 or width(t)>64: errs.append(f'{code}/{pid} title len={len(t)} width={width(t)} {t}')
                w=width(d)
                if w>160 or len(d)>155 or w<140: errs.append(f'{code}/{pid} desc len={len(d)} width={w} {d}')
            else:
                if len(t)>60 or (code=='th' and glen(t)>60): errs.append(f'{code}/{pid} title len={len(t)} glen={glen(t)} {t}')
                if not 140<=len(d)<=155 or (code=='th' and glen(d)>160): errs.append(f'{code}/{pid} desc len={len(d)} glen={glen(d)} {d}')
            link=data['links'][topic]
            if '{L}guide/' not in link or '{L}travel-guide/' not in link or 'href="{L}"' not in link:
                errs.append(f'{code}/{topic} links missing')
            has_fam='{L}guide/hcmc-with-family/' in link
            if (code in EXTRA)!=has_fam:
                errs.append(f'{code}/{topic} family link {has_fam}')
            if link.count('<a ') not in (3,4):
                errs.append(f'{code}/{topic} anchor count')
            if '{guide}' in link or '{guide}' in data['book']:
                errs.append(f'{code}/{topic} bare guide token')
        text='\n'.join(blob+[data['book'],data['hub_h2'],data['hub_p'],json.dumps(data['cards'],ensure_ascii=False)])
        if '!' in text or '！' in text:
            errs.append(code+' exclamation in blob')
        for rx,name in ((bad,'bad'),(bad2,'bad2')):
            m=rx.search(text)
            if m: errs.append(f'{code} {name}:{m.group(0)}')
        # one sentence in the booking line: no second terminal before the button
        book=data['book'].rstrip()
        if not book or book[-1] not in '.。．۔।':
            errs.append(code+' book ending '+book[-1:])
    return errs

def apply():
    for code, data in DATA.items():
        path=os.path.join(ROOT,'content',code+'.json')
        d=json.load(open(path,encoding='utf-8'))
        d['pages'].update(assemble(code, data))
        secs=d['pages']['guide']['sections']
        secs[:]=[s for s in secs if not s.get('_guest_notes')]
        block=hub(data)
        if secs and secs[-1].get('cta'):
            secs.insert(len(secs)-1, block)
        else:
            secs.append(block)
        raw=json.dumps(d,ensure_ascii=False,indent=1)
        open(path,'w',encoding='utf-8').write(raw)
    print('updated', ','.join(sorted(DATA)))

def main():
    add_vi(); add_zh()
    import guest_notes_rest
    guest_notes_rest.register(DATA, page, S, L)
    errs=validate()
    if errs:
        print('\n'.join(errs))
        print(len(errs),'problems')
        sys.exit(1)
    if '--check' in sys.argv:
        print('ok', len(DATA), 'languages')
        return
    apply()

if __name__=='__main__':
    main()
